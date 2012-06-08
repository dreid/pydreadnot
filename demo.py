from dreadnot import Dreadnot

# Connect to a dreadnot instance
dc = Dreadnot('http://localhost:8000', auth=('dreadnot', 'dreadnot'))

# List all the stacks and take the first one.
stack = dc.stacks()[0]

# List all the regions for that stack and take the first one.
region = dc.regions(stack['name'])[0]

# Deploy the latest revision of the stack to the first region.
print "Deploying: {0} in region {1}".format(stack['name'], region['name'])
print "  revision: {0}".format(stack['latest_revision'])

deploy = dc.deploy(stack['name'], region['name'], stack['latest_revision'])

print "    deploy: {0}".format(deploy['name'])

# Wait for the deploy to finish.
while not deploy['finished']:
    deploy = dc.deployment('tapkick', 'all', deploy['name'])

# Print the status of the deploy.
print "Deploy finished:", deploy['success'] and "Succeeded" or "failed"
