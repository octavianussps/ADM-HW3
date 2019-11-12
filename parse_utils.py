


def PLOT(tag_i, plot):
    # read all paragraph after Plot, removing everything bethween such as tables or pictures
    while tag_i.name != 'p':
        tag_i = tag_i.find_next_sibling()
    while tag_i.name == 'p':
        plot.append(tag_i.text[:-2])
        tag_i = tag_i.find_next_sibling()
    return plot

def INTRO(all_p_i,plot,intro):
    #select all the paragraph writen after the plot
    if plot=='NA':
        try:
            return all_p_i[0]
        except:
            return 'NA'
    else:
        for par in all_p_i:
            if par.text[:-2] == plot:
                break
            else:
                intro.append(par.text[:-2])
    return intro


def DICT_INFOBOX(soup_i,result):
    table = soup_i.find('table', class_='infobox vevent')
    for tr in table.find_all('tr'):
        if tr.find('th'):
            result[tr.find('th').text] = tr.get_text(strip=True, separator=" ")[len(tr.find('th').text):]#[m.text for m in tr.find_all('td')]#[len(tr.find('th')):]
        else:
            pass
    return result

def EMPTY_INFOBOX():
    a = {'Directed by': 'NA',
             'Produced by': 'NA',
             'Written by': 'NA',
             'Starring': 'NA',
             'Music by': 'NA',
             'Release date': 'NA',
             'Running time': 'NA',
             'Country': 'NA',
             'Language': 'NA',
             'Budget': 'NA'}
    return a






