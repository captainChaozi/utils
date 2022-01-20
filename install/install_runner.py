import os


def install_runner():
    # 创建配置文件
    HSCUSCODE = input("请输入Runner代号:")
    KEY = input("请输入KEY:")
    print(HSCUSCODE)
    s1 = os.system("sudo docker run --rm -t -i -v /etc/gitlab-runner:/etc/gitlab-runner gitlab/gitlab-runner register \
                   -n -u https://gitlab.com/ -r {key} --executor docker --docker-image docker \
                   --tag-list {hscode}".format(key=KEY,hscode=HSCUSCODE))
    assert s1 == 0, "runner配置失败"
    os.system("sudo chmod 777 /etc/gitlab-runner/config.toml")
    with open('/etc/gitlab-runner/config.toml', 'r') as f:
        s = f.read()
        a = s.replace(' volumes = ["/cache"]',
                      'volumes = ["/var/run/docker.sock:/var/run/docker.sock","/cache"]')
    with open('/etc/gitlab-runner/config.toml', 'w') as f:
        f.write(a)
    s2 = os.system("sudo docker run -d --name gitlab-runner --restart always \
                   -v /etc/gitlab-runner:/etc/gitlab-runner \
                   -v /var/run/docker.sock:/var/run/docker.sock \
                   gitlab/gitlab-runner:latest")
    assert s2 == 0, "安装runner失败"
    s3 = os.system("sudo docker restart gitlab-runner")
    assert s3 == 0, "runner 配置成功"
    print("安装runner成功")


if not os.path.exists('/etc/gitlab-runner'):
    install_runner()
    print("runner安装成功")