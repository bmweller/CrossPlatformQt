#ifndef HELPER_H
#define HELPER_H

#include <QObject>

class Helper : public QObject
{
    Q_OBJECT
public:
    explicit Helper(QObject *parent = 0);
    static bool dbConnect();
    
signals:
    
public slots:
    
};

#endif // HELPER_H
