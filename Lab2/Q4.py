import random

class SystemComponent:
    def __init__(self, name):
        self.name = name
        self.status = random.choice(["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"])

    def patch(self):
        if self.status == "Low Risk Vulnerable":
            self.status = "Safe"

    def __str__(self):
        return f"Component {self.name}: {self.status}"

class UtilityBasedSecurityAgent:
    def __init__(self, components):
        self.components = components

    def scan_system(self):
        print("System Scan Results:")
        for component in self.components:
            if component.status == "Safe":
                print(f"{component.name} is Safe.")
            else:
                print(f"Warning: {component.name} is {component.status}.")

    def patch_vulnerabilities(self):
        print("\nPatching Vulnerabilities:")
        for component in self.components:
            if component.status == "Low Risk Vulnerable":
                print(f"Patching Low Risk Vulnerability in {component.name}...")
                component.patch()
            elif component.status == "High Risk Vulnerable":
                print(f"{component.name} has a High Risk Vulnerability. Premium service required to patch.")

    def display_system_status(self, title):
        print(f"\n{title}")
        for component in self.components:
            print(component)

# Initialize system environment with components A through I
components = [SystemComponent(name) for name in "ABCDEFGHI"]

# Instantiate the Utility-Based Security Agent
agent = UtilityBasedSecurityAgent(components)

# Initial System Check
agent.display_system_status("Initial System State")

# System Scan
agent.scan_system()

# Patching Vulnerabilities
agent.patch_vulnerabilities()

# Final System Check
agent.display_system_status("Final System State")
