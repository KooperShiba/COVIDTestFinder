## CURRENTLY SUPPORTED TESTS
### TARGET ð¯
- Ellume COVID-19 Rapid Antigen Home Test

- Access Bio Covid Rapid Test - 2ct

- FlowFlex Covid-19 Antigen Home Test

### WALMART ð
- BinaxNOW COVIDâ19 Antigen Self Test (2 Count)




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
âï¸ Seperate functionality into smaller functions.

âï¸ Get all xPath variables into a single configuration file for easy and reliable updates.

âï¸ Seperate each retail store into it's own file and have a runner.

âï¸ Write an easy set-up guide in GitHub.

âï¸ Start work on a Telegram bot that takes zip codes as input.

âï¸ Write small guide on how xPaths were gathered.

â Figure out how to bipass Walmart's bot protections for complete automation.

â Find reliable alternative from doing this:
```
service = Service(executable_path=ChromeDriverManager().install())
```

## Current Issues
â ï¸ Zip Codes is being used as a global variable when it should be passed in as an arguement.

â ï¸ Walmart brute force function fails on second attempt.

â ï¸ Target second page type is not accounted for.
