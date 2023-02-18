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

#### What languages/packages/frameworks can I use for the example implementation? 

Please focus on implementation examples in 

- Python (preferred)
- JavaScript
- TypeScript 

as our current infrastructure can only test code iin these languages. 

In the example implementations, please only use the standard libraries and the following additional dependencies: 

Python:
- [`pandas`]()
- [`numpy`]() 

JavaScript/TypeScript:
  - [crypto-md5](#crypto-md5)
  - [base64-js](#base64-js)
  - [fast-xml-parser](#fast-xml-parser)
  - [jszip]([jszip])
  - [node-gzip](#node-gzip)
  - [pako](#pako)
  - [papaparse](#papaparse)
  - [xlsx](#xlsx)
  - [ml-matrix](#ml-matrix)
  - [fft.js](#fft.js)
  - [Array](#array)
  - [Array XY](#array-xy)


#### How do I structure the code example?

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

