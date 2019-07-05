# Docker for API

You can build and run the docker using the following process:

Cloning
```console
git clone https://github.com/jqueguiner/XXXX.git email-extractor
```

Building Docker
```console
cd email-extractor && docker build -t email-extractor -f Dockerfile .
```

Running Docker
```console
echo "http://$(curl ifconfig.io):5000" && docker run -p 5000:5000 -d email-extractor
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/process" -H "accept: application/json" -H "Content-Type: application/json" -d '{"url":"https://i.ibb.co/FqDSQF8/input.jpg"}'
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/detect" -H "accept: application/json" -H "Content-Type: application/json" -d '{"url":"https://i.ibb.co/FqDSQF8/input.jpg"}'
```
