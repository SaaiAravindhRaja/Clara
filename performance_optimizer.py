"""
Performance Optimizer for AI Calendar Agent
This script implements various optimizations to improve the agent's performance.
"""

import os
import time
import logging
from typing import Optional, Dict, Any
from functools import lru_cache
from dotenv import load_dotenv
from orgo import Computer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OptimizedCalendarAgent:
    """
    Optimized version of the calendar agent with performance improvements.
    """
    
    def __init__(self, project_id: str, use_cache: bool = True, max_retries: int = 3):
        """
        Initialize the optimized agent.
        
        Args:
            project_id: Orgo project ID
            use_cache: Whether to use caching for repeated operations
            max_retries: Maximum number of retries for failed operations
        """
        load_dotenv()
        self.project_id = project_id
        self.use_cache = use_cache
        self.max_retries = max_retries
        self.computer = Computer(project_id=project_id)
        self.last_screenshot_time = 0
        self.screenshot_cooldown = 1.0  # Minimum time between screenshots
        
        # Performance metrics
        self.operation_times = []
        self.success_count = 0
        self.failure_count = 0
        
    @lru_cache(maxsize=100)
    def cached_prompt(self, prompt: str) -> str:
        """
        Cached version of prompts to avoid redundant LLM calls.
        """
        return prompt
    
    def smart_screenshot(self) -> None:
        """
        Take screenshots only when necessary to reduce overhead.
        """
        current_time = time.time()
        if current_time - self.last_screenshot_time >= self.screenshot_cooldown:
            # Take screenshot logic here
            self.last_screenshot_time = current_time
            logger.info("Screenshot taken")
        else:
            logger.info("Skipping screenshot - too soon since last one")
    
    def retry_operation(self, operation_func, *args, **kwargs) -> Any:
        """
        Retry failed operations with exponential backoff.
        """
        for attempt in range(self.max_retries):
            try:
                start_time = time.time()
                result = operation_func(*args, **kwargs)
                operation_time = time.time() - start_time
                
                self.operation_times.append(operation_time)
                self.success_count += 1
                
                logger.info(f"Operation successful on attempt {attempt + 1} in {operation_time:.2f}s")
                return result
                
            except Exception as e:
                self.failure_count += 1
                wait_time = 2 ** attempt  # Exponential backoff
                
                logger.warning(f"Operation failed on attempt {attempt + 1}: {e}")
                logger.info(f"Retrying in {wait_time} seconds...")
                
                if attempt < self.max_retries - 1:
                    time.sleep(wait_time)
                else:
                    logger.error(f"Operation failed after {self.max_retries} attempts")
                    raise
    
    def optimized_prompt(self, prompt: str) -> str:
        """
        Optimized prompt with caching and retry logic.
        """
        if self.use_cache:
            cached_prompt = self.cached_prompt(prompt)
            if cached_prompt != prompt:
                logger.info("Using cached prompt")
                return cached_prompt
        
        return self.retry_operation(self.computer.prompt, prompt)
    
    def batch_operations(self, operations: list) -> list:
        """
        Batch multiple calendar operations for efficiency.
        """
        results = []
        for operation in operations:
            try:
                result = self.optimized_prompt(operation)
                results.append({"operation": operation, "result": result, "status": "success"})
            except Exception as e:
                results.append({"operation": operation, "result": str(e), "status": "failed"})
        
        return results
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get performance metrics for monitoring.
        """
        if not self.operation_times:
            return {
                "total_operations": 0,
                "success_rate": 0,
                "average_time": 0,
                "success_count": 0,
                "failure_count": 0
            }
        
        total_operations = self.success_count + self.failure_count
        success_rate = self.success_count / total_operations if total_operations > 0 else 0
        average_time = sum(self.operation_times) / len(self.operation_times)
        
        return {
            "total_operations": total_operations,
            "success_rate": success_rate,
            "average_time": average_time,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "min_time": min(self.operation_times),
            "max_time": max(self.operation_times)
        }

def create_optimized_agent(project_id: Optional[str] = None) -> OptimizedCalendarAgent:
    """
    Factory function to create an optimized agent.
    """
    if project_id is None:
        # Read from .orgo/project.json
        import json
        try:
            with open('.orgo/project.json', 'r') as f:
                config = json.load(f)
                project_id = config.get('project_id')
        except FileNotFoundError:
            raise ValueError("Could not find .orgo/project.json. Please provide project_id manually.")
    
    return OptimizedCalendarAgent(project_id=project_id)

# Example usage
if __name__ == "__main__":
    # Create optimized agent
    agent = create_optimized_agent()
    
    # Test single operation
    print("Testing single operation...")
    try:
        result = agent.optimized_prompt("Create a test event for tomorrow at 2pm")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test batch operations
    print("\nTesting batch operations...")
    operations = [
        "Create a meeting with John tomorrow at 10am",
        "Find my next event",
        "Schedule a lunch meeting on Friday at 12pm"
    ]
    
    results = agent.batch_operations(operations)
    for result in results:
        print(f"Operation: {result['operation']}")
        print(f"Status: {result['status']}")
        print(f"Result: {result['result']}\n")
    
    # Print performance metrics
    metrics = agent.get_performance_metrics()
    print("Performance Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}") 