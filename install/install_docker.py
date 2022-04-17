import os


def install_docker():
    step1 = os.system("wget -qO- https://get.docker.com/ | sh")
    assert step1 == 0, "docker 安装失败"
    step2 = os.system('sudo usermod -aG docker $USER')
    assert step2 == 0, "docker 用户组更改失败"
    os.system("sudo mkdir -p /etc/docker")
    with open('/etc/docker/daemon.json','rw') as f:
        f.write('{"registry-mirrors": ["https://m6wlkecl.mirror.aliyuncs.com"]}')
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl restart docker")
    print("docker安装成功")


if __name__ == "__main__":
    install_docker()