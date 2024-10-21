### Income Tax Calculator

## Overview
This Django-based Income Tax Calculator provides a comprehensive and user-friendly tool for calculating income tax based on appropriate tax slabs. The application offers a detailed breakdown of tax liability and includes visual representations using Chart.js for enhanced understanding.

## Features
- Accurate tax calculation based on current tax slabs.
- Detailed breakdown of tax liability for each slab.
- Visual representation of tax distribution using Chart.js.
- User-friendly interface designed with Tailwind CSS.
- Server-side rendering using Django templates for fast and efficient performance.

## Live Project Link
Check out the live version of the application here: [Live Link](https://income-tax-calculator-alpha.vercel.app/)


## Technologies Used
- **Django**: Web framework for building the application.
- **Tailwind CSS**: For responsive and modern UI design.
- **Chart.js**: For creating interactive and visually appealing charts.
- **Python**: Core programming language.
- **HTML/CSS**: For structuring and styling web pages.

## SOLID Principles Implementation
This project adheres to SOLID principles to ensure clean, maintainable, and extensible code:
- **Single Responsibility Principle**: Each class and function has a single, well-defined responsibility.
- **Open-Closed Principle**: The tax calculation logic is designed to be easily extendable for new tax slabs without modifying existing code.
- **Liskov Substitution Principle**: Any derived classes (if applicable) can be substituted for their base classes without affecting the correctness of the program.
- **Dependency Inversion Principle**: High-level modules do not depend on low-level modules. Both depend on abstractions.

## How It Works
1. Users input their income and other relevant financial details.
2. The application calculates the tax liability based on the current tax slabs.
3. A detailed breakdown of the tax calculation is displayed, showing the amount payable in each slab.
4. A chart is generated using Chart.js to visually represent the distribution of tax across different slabs.
