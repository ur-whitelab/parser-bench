# parser-bench

## structure 

For each filetype there is one directory with multiple subdirectories:

```
myfiletype
    meta.json
    example_implementations
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

### Example implementations

Check `data/zeopp-sa` for an example 

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