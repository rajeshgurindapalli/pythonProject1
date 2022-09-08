import flask.client as flask
olApp = flask.Dispatch('Outlook.Application')
olNS =olApp.GetNameSpace('MAPI')
mailItem= olApp.CreateItem(0)
mailItem.Subject='Hello sir this is 2100030973'
mailItem.BodyFormat = 1
mailItem.Body ="HELLO SIR THIS IS JUST AN PFSD-FLASK MAIL USING SQL lite3"
mailItem.To='2100030261@kluniversity.in'
mailItem._oleobj_.Invoke(*(64209,0,8,0,olNS.Accounts.Item('2100030973@kluniversity.in')))
mailItem.Display()
mailItem.Save()
mailItem.Send()