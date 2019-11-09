# Better shit

gimmie hugs!!!!!!!!!!!!!!!!!!!!!!!!!!!!! (affection is so fun fun fun ufn fun)

(this is a brightness analyzer using flask lul noobs)

*notice me senpaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii*

## Actual Readme

you can make get requests to the following url locations for data

For actual demo: Port num: `4200`

- `/test/list`: Returns a list of all valid tests
- `/test/img/<path>`: 
    - Runs the analyzer on one of the test images
    - `<path>` can be one of the following: `test1`, `test2`, `test3`
- `/test/b64/<path>`:
    - Converts one of the test images to base64 and returns it
    - Altchars used: `+-` (instead of `+/`)
    - `<path>` can be one of the following: `test1`, `test2`, `test3`
- `/img/<blob>`:
    - Runs the analyzer on the given `blob`
        - `blob` is a base64 string (specs below) that contains the data of the image
        - The image should be in `jpeg` format
        - **For base64: Altchars used: `+-` (instead of `+/`)**
- `/`:
    - Returns `Hello World!`
