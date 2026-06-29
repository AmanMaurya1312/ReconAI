from models.target import Target
from scanners.subfinder import SubfinderScanner

target = Target(
    domain="tesla.com"
)

scanner = SubfinderScanner(target)

result = scanner.run()

print(result)
