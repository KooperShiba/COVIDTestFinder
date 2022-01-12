# COVIDTestFinder

## CURRENTLY SUPPORTED TESTS
### TARGET 🎯
- Ellume COVID-19 Rapid Antigen Home Test

- Access Bio Covid Rapid Test - 2ct

- FlowFlex Covid-19 Antigen Home Test

### WALMART 🛒
- BinaxNOW COVID‐19 Antigen Self Test (2 Count)




## Dependancies
To resolve all project dependacies, please download the requrements.txt file. Run the following command in a Windows command prompt:
```
pip3 install -r requirements.txt
```
or
```
pip3 install -r requirements.txt --user
```

## To Do
✍️ Seperate functionality into smaller functions

✍️ Get all xPath variables into a single configuration file for easy and reliable updates

✍️ Seperate each retail store into it's own file and have a runner

✍️ Write an easy set-up guide in GitHub

✍️ Start work on a Telegram bot that takes zip codes as input

✍️ Write small guide on how xPaths were gathered.

❓ Figure out how to bipass Walmart's bot protections for complete automation

❓ Find reliable alternative from doing this:
```
service = Service(executable_path=ChromeDriverManager().install())
```

## Current Issues
⚠️ Zip Codes is being used as a global variable when it should be passed in.

⚠️ Walmart brute force function fails on second attempt.

⚠️ Target second page type is not accounted for
