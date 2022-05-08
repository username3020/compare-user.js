# compare-user.js
A python application to compare multiple user.js files.

The user.js of Firefox allows to configure your browser to your needs. There are different examples out there, but to manually compare them with each other takes time. This python application allows to print out a summary about the differences of two user.js files as input.

Additionally it allows to print the differences in the format of the user.js files when used with the parameter `-printLines`

## Requirements

Install dependencies with pip:

`pip install dictdiffer tabulate`

Or install with

`pip install -r requirements.txt`


## Usage

Just compare two files an get difference summary (added values, removed values, changed values):

`python3 compare.js user.js user.custom.js`

Same as above, but also prints out the values in user.js format, so they can be easily integrated in your files.

`python3 compare.js user.js user.custom.js -printLines`



## Sources for user.js files

There are projects like [Arkenfox/user.js](https://github.com/arkenfox/user.js/) or [pyllyukko/user.js](https://github.com/pyllyukko/user.js/) which provide customized user.js files.


## Example output

```
> python3 compare.py user.js user.custom.js
Differences between user.js and user.custom.js:
| Name                               | user.js                                | user.custom.js   |
|------------------------------------+----------------------------------------+------------------|
| keyword.enabled                    | false                                  | true             |
Only in user.js
| Name   | Setting   |
|--------+-----------|
Only in user.custom.js
| Name                                                                              | Setting                                                                    |
|-----------------------------------------------------------------------------------+----------------------------------------------------------------------------|
| general.warnOnAboutConfig                                                         | false                                                                      |
Removed in user.js
| Name   | Setting   |
|--------+-----------|
Removed in user.custom.js
| Name                                                      | Setting       |
|-----------------------------------------------------------+---------------|
| browser.startup.page                                      | 0             |
```
