# Docker for API

You can build and run the docker using the following process:

Cloning
```console
git clone https://github.com/jqueguiner/email-extraction.git email-extraction
```

Building Docker
```console
cd email-extraction && docker build -t email-extraction -f Dockerfile .
```

Running Docker
```console
echo "http://$(curl ifconfig.io):5000" && docker run -p 5000:5000 -d email-extraction
```

Calling the API
```console
curl -X POST "http://MY_SUPER_API_IP:5000/detect" -H "accept: application/json" -H "Content-Type: application/json" -d '{"text":"lorem ipsum linuxhack@att.net lorem ipsum fwitness@me.com"}'
```
