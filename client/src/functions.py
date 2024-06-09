import matplotlib.pyplot as plt


def draw_hist(preds):
    counts = {0: 0, 1: 0}
    for pred in preds:
        counts[pred] += 1

    # Строим столбчатую диаграмму
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values())

    # Добавляем заголовок и метки осей
    ax.set_title('Class Distribution')
    ax.set_xlabel('Class')
    ax.set_ylabel('Count')

    # Добавляем подписи к столбцам
    for class_label, count in counts.items():
        ax.text(class_label, count, str(count), ha='center', va='bottom')

    return fig


def download_link(object_to_download, download_filename,
                  href, download_link_text):
    """
    Функция для создания ссылки для скачивания объекта.
    """
    lk = str(f'<a href="{href},{object_to_download}" download=' +
             f'"{download_filename}" target="_blank">{download_link_text}</a>')
    return lk
