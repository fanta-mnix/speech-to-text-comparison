from Levenshtein import distance


def ratio(t1, t2):
    return 1 - float(distance(t1, t2))/max(len(t1), len(t2))


audio1 = '''amigos são poucos e escassos ao longo da vida e esta é uma lição que eu duramente aprendi nós temos centenas de conhecidos mas temos poucos amigos e eu já lancei uma vez e volta a dizer que é um teste eficaz infalível para vocês aplicarem sobre a amizade ao retornarem às suas casas ao longo dos próximos dias reunam os amigos e digam sobre o sucesso de vocês não falem de fracasso o fracasso provoca solidariedade entre todas as pessoas o fracasso provoca proximidade entre as pessoas se eu disser que tem um câncer receberei abraços todas as pessoas'''.lower()

bing1 = '''amigos são poucos e escassos ao longo da vida eh essa é uma lição que eu duramente aprende nós temos centenas de conhecidos mas temos poucos amigos e eu já lancei uma vez de volta dizer que é um teste e ficas infalível pra vocês aplicarem sobre amizade ao retornarem às suas casas ao longo dos próximos dias reuniu os amigos e digam sobre o sucesso de vocês não falem de fracasso em fracasso provoca solidariedade entre todas as pessoas ou fracasso provoca proximidade entre as pessoas se eu disser que tem um câncer receberia braços todas as pessoas'''.lower()

google1 = '''amigos são poucos e escassos ao longo da vida e esta é uma lição que eu duramente aprende nós temos centenas de conhecidos mas temos poucos amigos e eu já lancei uma vez de volta dizer que é um teste eficaz alívio para vocês aplicar em sobre amizade ao retornarem às suas casas ao longo dos próximos dias eu não os amigos e digam sobre o sucesso de você não falem de fracasso em fracasso provoca solidariedade entre todas as pessoas o fracasso provoca proximidade entre as pessoas se eu disser que tem um câncer receberei abraços todas as pessoas'''.lower()

watson1 = '''amigo são poucos e escassos ao longo da vida e esta é uma lição que o dura mente aprende aos termos centenas de conhecidos mas temos poucos amigos e os balanceio uma vez e volta a dizer que é um teste e fica às infalível para vocês aplicarem sobre amizade ao retornarem a suas que reúnam os amigos digam sobre o sucesso não falem os fracassos o fracasso provoca solidariedade de todas as pessoas o fracasso provoca proximidade entre as se eu disse é que tem um câncer receberia braços todas as pessoas'''.lower()

audio2 = '''Além disso você quiser usar o microfone de lapela ligado diretamente na câmera o fio desse microfone vai ter que ser bem comprido um fio bem comprido por onde tá passando o sinal fraco como de um microfone vira uma bela antena e é muito fácil pegar a interferência eletromagnética com um fio de microfone que é Longe de mais além disso quanto maior o fio maior a chance de alguém tropeçar no fio e mandar sua câmera para o chão se esses problemas não te incomoda usar o microfone ligado diretamente na câmera na verdade é uma boa alternativa e mais uma coisa essas informações não se aplicam no caso de câmeras profissionais e a câmera de microfones com conexão XLR essas conexões são praticamente a prova de interferência e se uma câmera tem entrada XLR a chance dela tem um pré-amplificador de baixo qualidade é muito pequena'''.lower()

bing2 = '''além disso se você quiser usar o microfone de lapela ligado diretamente na camera ou field's microfone ptc bem cumprido um filme comprido porque onde tá passando o sinal fraco como de o microfone numa bela antenatal muito fácil pegar interferência eletromagnética um filme microfone que é longo demais além disso quanto maior o phil maiores chances de alguém tropeçou no fio de mandar sua camera pro chão seus problemas não te incomodam usar o microfone ligado diretamente na camera na verdade é uma boa tentativa ah mais uma coisa essas informações não se aplicam no caso de câmeras profissionais e câmeras microfones com conexão xlr essas conexões são praticamente a prova de interferência esse uma camera temporada salieri a chance dela ter um pré amplificador de baixa qualidade é muito pequena'''.lower()

google2 = '''Além disso você quiser usar o microfone de lapela ligado diretamente na câmera o seu desse microfone vai ter que ser bem Comprido um fio bem comprido para Onde tá passando o sinal fraco como de um microfone vir uma bela antena que é muito fácil pegar a interferência eletromagnética com um fio de microfone que é Longe de mais além disso quanto maior o fio maior a chance de alguém tropeçar no fio e mandar sua câmera para o chão problemas não te incomoda usar o microfone ligado diretamente na câmera na verdade é uma boa alternativa e mais uma coisa essas informações não se aplicam no caso de câmeras profissionais e a câmera de microfones com conexão XLR essas conexões são praticamente a prova de interferência e se uma câmera tem entrada XLR a chance dela tem um pré-amplificador de baixo qualidade é muito pequeno'''.lower()

watson2 = '''além disso se você quiser usar o microfone de lapela ligado diretamente na câmara o fio das microfone pertencer bem cumprido um fio bem cumprido por prós tapação num sinal fraco como de um microfone vira uma bela antena é muito fácil pegar interferência das magnética com que os microfones é longo demais além disso quanto maior o fio maiores chances de alguém tropeçar no filme e mandasse canetas chão se os problemas não se incomodam os ao microfone ligado diretamente na câmara na verdade é uma boa alternativa a e mais uma coisa essas informações não se aplicam no caso de câmeras profissionais e para câmeras microfones com conexão gisele é essas conexões são praticamente a prova de interferências existe uma câmera tem cargos aliás as chances da otan pré-amplificador de baixa qualidade é muito pequena'''.lower()


summary = '''
| Empresa | Áudio 1 | Áudio 2 |
|---------|---------|---------|
| Bing    |   {:.3f} | {:.3f}   |
| Google  |   {:.3f} | {:.3f}   |
| Watson  |   {:.3f} | {:.3f}   |
'''.format(
    ratio(audio1, bing1),
    ratio(audio2, bing2),
    ratio(audio1, google1),
    ratio(audio2, google2),
    ratio(audio1, watson1),
    ratio(audio2, watson2))

print(summary)
