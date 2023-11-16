import subprocess

def install_tools():
    try:
        subprocess.run(["cd", "home/"], check=True)
        subprocess.run(["apt", "update"], check=True)
        subprocess.run(["apt", "install", "nano", "-y"], check=True)
        subprocess.run(["apt", "install", "pip", "-y"], check=True)
        subprocess.run(["apt", "install", "net-tools -y"], check=True)
        subprocess.run(["apt", "install", "wget -y"], check=True)
        subprocess.run(["wget", "https://go.dev/dl/go1.21.4.linux-amd64.tar.gz"], check=True)
        subprocess.run(["rm", "-rf", "/usr/local/go"], check=True)
        subprocess.run(["tar", "-C", "/usr/local", "-xzf", "go1.21.4.linux-amd64.tar.gz"], check=True)
        subprocess.run(["export", "PATH=$PATH:/usr/local/go/bin"], check=True)
        subprocess.run(["go", "install", "-v", "github.com/tomnomnom/anew@latest"], check=True)
        subprocess.run(["cp", "/root/go/bin/anew", "/usr/bin/"], check=True)
        subprocess.run(["pip", "install", "\'httpx[cli]\'"], check=True)
        print("All tools installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

# Chamando a função para instalar o Nmap
if __name__ == "__main__":
    install_tools()
