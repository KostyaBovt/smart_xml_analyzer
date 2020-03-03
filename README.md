# Smart XML Analyzer


## How to install

1. `git clone https://github.com/KostyaBovt/smart_xml_analyzer.git folder`
2. `cd folder`
3. `virtualenv -p python3 venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`


## How to run
* `python app.py  <input_origin_file_path> <input_other_sample_file_path>`
* `python app.py  <input_origin_file_path> <input_other_sample_file_path> <custom_id_for_element_in_origin_file>`


## Algorithm
* Get target element from origin page by id
* Get all attributes of target element
* Get tag name of target elements (orig_tag)
* Get all elements from other sample page with orig_tag
* Count for every found elements (on previous step) in sample page: amount of attributes equal to attributes of orig element
* Element with max attributes equal to origin element attributes is found element


## Some analytics based on provided samples
| attr          | 0 - origin page                               | 1 - sample page                               | 2 - sample page                                   | 3 - sample page                               | 4 - sample page                                   |
|---------------|-----------------------------------------------|-----------------------------------------------|---------------------------------------------------|-----------------------------------------------|---------------------------------------------------|
| id            | **make-everything-ok-button**                 |                                               |                                                   |                                               |                                                   |
| class         | **btn btn-success**                           | **btn btn-success**                           | btn test-link-ok                                  | **btn btn-success**                           | **btn btn-success**                               |
| href          | **#ok**                                       | #check-and-ok                                 | **#ok**                                           | **#ok**                                       | **#ok**                                           |
| title         | **Make-Button**                               | **Make-Button**                               | **Make-Button**                                   | Do-Link                                       | **Make-Button**                                   |
| rel           | **next**                                      | done                                          | **next**                                          | **next**                                      | **next**                                          |
| onclick       | **javascript:window.okDone(); return false;** | **javascript:window.okDone(); return false;** | javascript:window.okComplete(); return false;     | **javascript:window.okDone(); return false;** | javascript:window.okFinalize(); return false;     |
| text          | **Make everything OK**                        | **Make everything OK**                        | **Make everything OK**                            | Do anything perfect                           | Do all GREAT                                      |
| equal tags    | 7                                             | 4                                             | 4                                                 | 4                                             | 4                                                 |


## Examples
`$ python app.py samples/sample-0-origin.html samples/sample-1-evil-gemini.html`  
`html > body > div > div > div[3] > div[1] > div > div[2] > a[2]`

`$ python app.py samples/sample-0-origin.html samples/sample-2-container-and-clone.html`  
`html > body > div > div > div[3] > div[1] > div > div[2] > div > a`

`$ python app.py samples/sample-0-origin.html samples/sample-3-the-escape.html`  
`html > body > div > div > div[3] > div[1] > div > div[3] > a`

`$ python app.py samples/sample-0-origin.html samples/sample-4-the-mash.html`  
`html > body > div > div > div[3] > div[1] > div > div[3] > a`
