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
curl -X POST "http://MY_SUPER_API_IP:5000/detect" -H "accept: application/json" -H "Content-Type: application/json" -d '{"text":"Full match 4-21 linuxhack@att.net Match 2 Full match 26-41 fwitness@me.com  Match 3"}'
```
