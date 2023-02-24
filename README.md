# parser-bench

A dataset and benchmark for file to file parser construction with LLMs that write code. 

## structure 

For each filetype there is one directory with multiple subdirectories:


```
myfiletype
    meta.json
    implementations
        1
            meta.json
            parser.py
    inputs
        1.your_extension
        2.your_extension
    outputs
        1.json
        2.json
```

Check `data/zeopp-sa` for an example 

### FAQ

#### What do I get from contributing? 

Besides helping to advance science, meaningful contributions (i.e., merged PR adding an entry) will qualify for co-authorship on a paper (that might come out of this work).

#### What languages/packages/frameworks can I use for the example implementation? 

Please focus on implementation examples in 

- Python (preferred)
- JavaScript
- TypeScript 

as our current infrastructure can only test code in these languages. 

In the example implementations, please only use the standard libraries and the following additional dependencies: 

Python:
- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/) 

JavaScript/TypeScript:
  - [`crypto-md5`](https://www.npmjs.com/package/crypto-md5)
  - [`base64-js`](https://www.npmjs.com/package/base64-js)
  - [`fast-xml-parser`](https://www.npmjs.com/package/fast-xml-parser)
  - [`jszip`](https://www.npmjs.com/package/jszip)
  - [`node-gzip`](https://www.npmjs.com/package/node-gzip)
  - [`pako`](https://www.npmjs.com/package/pako)
  - [`papaparse`](https://www.npmjs.com/package/papaparse)
  - [`xlsx`](https://www.npmjs.com/package/xlsx)
  - [`ml-matrix`](https://www.npmjs.com/package/ml-matrix)
  - [`fft.js`](https://www.npmjs.com/package/fft-js)
  - [`Array`](https://www.npmjs.com/package/array)


#### How do I structure the code example?

Please provide the implementation as function that accepts the file as string and returns the parsed `json` string.
### Validating the data 


Install the package

```bash 
pip install -e .
```

Then run the validation 

```bash
parserbench.validate_dirs data/
```

## Related projects

- [chemical-files-registry](https://github.com/kjappelbaum/chemical-files-registry): started as registry for filetypes that are commonly used in chemistry

- [metadata_extractors_registry](https://github.com/marda-alliance/metadata_extractors_registry): started as part of the [MARDA](http://www.marda-alliance.org/) extractors working group

