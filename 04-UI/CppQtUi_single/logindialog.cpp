#include "logindialog.h"
#include "ui_logindialog.h"
#include <QMessageBox>

LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this);
}

LoginDialog::~LoginDialog()
{
    delete ui;
}

void LoginDialog::on_buttonBox_accepted()
{
    if(ui->txtUsername->text()=="admin")
    {
        setResult(LoginDialog::Success);
    }else{
        QMessageBox msgBox(this);
        msgBox.setIcon(QMessageBox::Warning);
        msgBox.setWindowTitle(tr("Pythonthusiast"));
        msgBox.setText(tr("Either incorrect username and/or password. Try again!"));
        msgBox.setStandardButtons(QMessageBox::Ok);
        msgBox.exec();

        setResult(LoginDialog::Failed);
    }
}

void LoginDialog::on_buttonBox_rejected()
{
    setResult(LoginDialog::Rejected);
}
