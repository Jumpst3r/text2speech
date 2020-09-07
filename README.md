## Dockerized text to speach

### Description

Read out text (text-to-speach), auto-detecting the input language

### Usage

To use the docker image, first pull the image using

`docker pull jumpst3r/text2speech

And then execute 
```
docker run -it --rm -v /FULL_PATH_TO/example.txt:/input/example.txt -v /FULL_PATH_TO_OUTPUT_FOLDER/:/output/ jumpst3r/text2speech sh /input/script.sh /input/example.txt /output/
```

where `/FULL_PATH_TO/example.rxt` corresponds to the local path of the input text file.

The output consists of:

- An audio file containing the spoken text

The docker image is also compatible with [DIVAServices](https://github.com/lunactic/DIVAServices) a web-based framework providing streamlined access to DOI methods.
