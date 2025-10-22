# rotating-image-server
very simple time-based rotating image server using python

## Setup (docker)

```bash
git clone https://github.com/wxnnvs/rotating-image-server
cd rotating-images-server
mkdir images
# put at least 1 image in the images folder (jpg, png, ...)
cp example-compose compose.yml
docker compose up --build -d
# http://localhost:6767
```