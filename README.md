# notification-service

## email templates

```
cd email_templates
aws ses create-template --cli-input-json file://template-1.json
aws ses update-template --cli-input-json file://template-1.json
aws ses send-templated-email --source "Deale <no-reply@deale.es>" --destination ToAddresses=tonitripiana@gmail.com --template template-1 --template-data "{ \"name\":\"Antonio\", \"sender\": \"Gerard\" }"
```
# bci4als_notification
