from setuptools import find_packages,setup

def get_requirements()->list[str]:
    requirements_lst: list[str] = []
    try:
        with open("requirements.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt is not found")
    return requirements_lst
setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Varun Vasaguddam",
    author_email = "varunvassagudam@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements()
)