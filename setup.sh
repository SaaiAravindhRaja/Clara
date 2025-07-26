#!/bin/bash

# AI Calendar Agent Setup Script
# This script automates the setup process for the AI Calendar Agent

echo "🚀 Setting up AI Calendar Agent..."

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed. Please install Anaconda or Miniconda first."
    echo "Download from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "orgo-env.yml" ]; then
    echo "❌ orgo-env.yml not found. Please run this script from the project root directory."
    exit 1
fi

# Create conda environment
echo "📦 Creating conda environment..."
conda env create -f orgo-env.yml

if [ $? -eq 0 ]; then
    echo "✅ Conda environment created successfully!"
else
    echo "❌ Failed to create conda environment. Please check the orgo-env.yml file."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔧 Creating .env file..."
    cat > .env << EOF
# API Keys - Replace with your actual keys
ORGO_API_KEY=your_orgo_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Browser path for macOS
BROWSER_EXECUTABLE_PATH=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
EOF
    echo "✅ .env file created! Please edit it with your actual API keys."
else
    echo "ℹ️  .env file already exists. Please make sure your API keys are set correctly."
fi

# Fix project ID in notebook
echo "🔧 Creating corrected notebook..."
if [ -f "src.ipynb" ]; then
    # Create a backup
    cp src.ipynb src_backup.ipynb
    echo "✅ Backup created as src_backup.ipynb"
fi

# Check if .orgo/project.json exists
if [ -f ".orgo/project.json" ]; then
    echo "✅ Found .orgo/project.json"
else
    echo "❌ .orgo/project.json not found. Please make sure you have set up your Orgo project."
fi

echo ""
echo "🎉 Setup complete! Next steps:"
echo ""
echo "1. Activate the environment:"
echo "   conda activate orgo-env"
echo ""
echo "2. Edit .env file with your API keys:"
echo "   nano .env"
echo ""
echo "3. Get your API keys from:"
echo "   - Orgo: https://www.orgo.ai/"
echo "   - OpenAI: https://platform.openai.com/"
echo "   - Anthropic: https://console.anthropic.com/"
echo ""
echo "4. Test the setup:"
echo "   python performance_optimizer.py"
echo ""
echo "5. Use the optimized notebook:"
echo "   jupyter lab src_fixed.ipynb"
echo ""
echo "📚 For more help, see SETUP_GUIDE.md" 