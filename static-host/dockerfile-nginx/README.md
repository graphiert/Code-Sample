# Docker with Nginx - Local server

How to set up:
1. Make sure you have a HTML file
  - With the name `index.html`
  - Being in the root of the project
2. If you want to add another file,
  - Create a folder, then put all assets in that folder
3. Do the image build process
  - `docker build -t <image:tag> .`
  - Make sure you already have a Docker Hub account,
  - and are logged in to the Docker CLI
4. Create container from created image, and start the container
  - `docker container create --name <name> --publish 8080:80 <image:tag>`
  - Start container: `docker container start <name>`
  - Stop container: `docker container stop <name>`
