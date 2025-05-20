#!/bin/bash
DATE=$(date +%F)
cp progress/template.md progress/$DATE.md
echo "New log created: progress/$DATE.md"