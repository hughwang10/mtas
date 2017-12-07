#--no-cache
repo='hugh/mtas'
docker image build --no-cache -t $repo .
docker rmi $(docker images -q --filter "dangling=true")
docker images | grep $repo