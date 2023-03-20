import matplotlib.pyplot as plt

def genera_pie_chart():
    labels = ["A","B","C"]
    values = [200, 400, 100]
    
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()