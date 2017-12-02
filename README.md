# pypyjs-examples-remix

This is a repository of more pypyjs examples. It's meant to demonstrate JavaScript code functionality along with the same exact functionality in Python.

I struggled through understanding [pypyjs-examples](https://github.com/pypyjs/pypyjs-examples) so I wanted to create some simpler demos for people to learn from.

# Use

This project submodules the [pypyjs-release](https://github.com/pypyjs/pypyjs-release) repo so you don't have to build it yourself. To get this project in working order run the below commands:

```bash
git clone git@github.com:adamyala/pypyjs-examples-remix.git
cd pypyjs-examples-remix
git submodule update --init --recursive
```

Once the repo is cloned and the submodules are initialized, run one of the two below commmands to serve the files:

```bash
# python2
python -m SimpleHTTPServer
# python3
python -m http.server
```

Once the server is running visit http://127.0.0.1:8000/, browse to and click on the file you wish to load.

## Running pypyjs examples

Loading pypyjs into a browser takes a bit of time (usually less than a second) and is a highly experimental process. When running the pypyjs examples in this repository it is recommended that you keep your browser's console open to look for errors.

Internet Explorer is not supported.

# Contents

Below is a description of each file.

<table>
    <thead>
        <tr>
            <th>File</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>button/button-js.html</td>
            <td>The most basic jQuery example in this repo</td>
        </tr>
        <tr>
            <td>button/button-py.html</td>
            <td>The most basic pypyjs wrapped jQuery example in this repo</td>
        </tr>
        <tr>
            <td>colorful/colorful-js.html</td>
            <td>A pure JavaScript example borrowed from this <a href="https://codepen.io/raftastrock/pen/paufw">codepen</a></td>
        </tr>
        <tr>
            <td>colorful/colorful-py.html</td>
            <td>The colorful-js example rewritten in pypyjs and python</td>
        </tr>
    </tbody>
</table>