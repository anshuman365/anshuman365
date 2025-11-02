#!/bin/bash
echo "Setting up new repository: $1"
mkdir $1
cd $1
git init
cat > README.md << 'EOL'
# $1

## Description
Project description goes here.

## Installation
\`\`\`bash
npm install
\`\`\`

## Usage
\`\`\`bash
npm start
\`\`\`
EOL
git add .
git commit -m "Initial commit"
echo "Repository $1 setup complete!"
