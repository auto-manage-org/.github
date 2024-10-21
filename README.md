This repository will apply peribolos to manage organization.


To use peribolos to manage organization, the base requirement is Go setup.
When running peribolos, it needs permission to access to the orgnization,
repository resources. The Github app installation access token has no
permission for endpoint user when peribolos updates members of orgnization.
The Github app user access token could help. A user access token only has
permissions that both the user and the app have. More details, please see
[Generating a user access token for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app).


# Prerequisites
- [Registered a Github app](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) and reccord the client ID
- [Installed the app](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app) with reasonable permission
- [Enable the 'device flow'](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-cli-with-a-github-app#about-device-flow-and-user-access-tokens) of the app
- [Generate a Github app user access token](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-cli-with-a-github-app#write-the-cli) via app_cli.rb
- Store the service account Github app user access token

# References


[Peribolos CLI](https://docs.prow.k8s.io/docs/components/cli-tools/peribolos/)


[Peribolos source](https://github.com/kubernetes-sigs/prow/tree/main/cmd/peribolos)
