# 5001 – Lab 3

##### Please use a markdown viewer or any web based markdown viewer

- Explaining the lines: -

  - FROM – This line is the image that you want to use for the docker image.
  - COPY[line 2] – This line copies from the index html file from source to nginx/html folder to be served by nginx
  - COPY[line 2] – This line copies the linux.png image from source to nginx/html folder to be served by nginx
  - EXPOSE – This line exposes the mentioned port (80 & 443) to the external networks
  - CMD – This is the commands that is executed during the start of the container.

- The steps from the build command are explained below:-

  - `Step 1/5 : FROM nginx:latest`
    > This setp pull image from the dockerhub and caches it locally
  - `Step 2/5 : COPY index.html /usr/share/nginx/html`
    > This step copies `index.html` from soruce to nginx/html for nginx to serve it out to the internet
  - `Step 3/5 : COPY linux.png /usr/share/nginx/html`
    > This step copies `linux.png` from source to nginx/html for nginx, this is required by index.html
  - `Step 4/5 : EXPOSE 80 443`
    > This step exposes port 80 & 443 to the public
  - `Step 5/5 : CMD ["nginx", "-g", "daemon off;"]`
    > This step executes the command to run nginx web-server that serves the website to the outside world

- We mounted the docker container that was already running to the host(`linux_tweet_app` dir) and edited the files inside that running docker image. Any changes made to the host directory (the current working directory) will be reflected in the container, and therefore, the running website. So, modifying the index.html file in the host directory would change the website that is being served by the NGINX server running in the container, even though a new image was not built after the modification.

- At first the 1.0 docker image was made fresh so it pushed all layers individually. But after that, the 2.0 docker image was made by mounting the running container to the host directory and editing the files. So, it pushed only modified layers of the image.

- The docker image is available at [Dockerhub](https://hub.docker.com/repository/docker/cruelplatypus67/linux_tweet_app/tags?page=1&ordering=last_updated)
