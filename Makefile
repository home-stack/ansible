all:
	$(info install - install the stuff)
	$(info clean - clean up)
install:
	./setup.sh
activate:
	. ./.home-stack-ansible/bin/activate
clean:
	rm -rf .ansible
