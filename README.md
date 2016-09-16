# 5_meetup Deep Learning SP

Bem vindos!

Pesquisa do Meetup

https://goo.gl/forms/6CqugTiu34qU68V42


## Montando o ambiente via Docker

Imagem docker utilizada: https://github.com/saiprashanths/dl-docker

### Passos para montar e utilizar a imagem

#### Se sua maquina NÃO tem uma boa placa de vídeo:

'''
git clone https://github.com/saiprashanths/dl-docker.git
cd dl-docker

docker build -t floydhub/dl-docker:cpu -f Dockerfile.cpu .

 # Trocar o /sharedfolder para a localizacao onde você quer salvar os notebooks na sua maquina
docker run -it -p 8888:8888 -p 6006:6006 -v /sharedfolder:/root/sharedfolder floydhub/dl-docker:cpu bash

jupyter notebook /root/sharedfolder/
'''

#### Se sua maquina NÃO tem uma boa placa de vídeo:

'''
git clone https://github.com/saiprashanths/dl-docker.git
cd dl-docker

docker build -t floydhub/dl-docker:gpu -f Dockerfile.gpu .

 # Trocar o /sharedfolder para a localizacao onde você quer salvar os notebooks na sua maquina
nvidia-docker run -it -p 8888:8888 -p 6006:6006 -v /sharedfolder:/root/sharedfolder floydhub/dl-docker:gpu bash

jupyter notebook /root/sharedfolder/
'''

