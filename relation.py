################################################################################################################################徐凯成
import re
_filter = [
    # 表亲
    {  # 表亲的关系
        'exp': r'^(.+)&o([^#]+)&l',
        's': r'\g<1>\g<2>'
    },
    {  # 表亲的关系
        'exp': r'^(.+)&l([^#]+)&o',
        's': r'\g<1>\g<2>'
    },
    {  # 表亲的关系
        'exp': r'(,[ds],(.+),[ds])&[ol]',
        's': r'\g<1>'
    },
    # 兄弟姐妹
    {  # 哥哥姐姐的哥哥姐姐还是自己的哥哥姐姐(年龄判断)
        'exp': r'(,o[sb])+(,o[sb])',
        's': r'\g<2>'
    },
    {  # 弟弟妹妹的弟弟妹妹还是自己的弟弟妹妹(年龄判断)
        'exp': r'(,l[sb])+(,l[sb])',
        's': r'\g<2>'
    },
    {  # 如果自己是男性,兄弟姐妹的兄弟就是自己的兄弟或自己
        'exp': r'^(.*)(,[fh1])(,[olx][sb])+,[olx]b(.*)$',
        's': r'\g<1>\g<2>,xb\g<4>#\g<1>\g<2>\g<4>'
    },
    {  # 如果自己是女性,兄弟姐妹的姐妹就是自己的姐妹或自己
        'exp': r'^(.*)(,[mw0])(,[olx][sb])+,[olx]s(.*)$',
        's': r'\g<1>\g<2>,xs\g<4>#\g<1>\g<2>\g<4>'
    },
    {  # 如果自己是男性,兄弟姐妹的姐妹就是自己的姐妹
        'exp': r'(,[fh1])(,[olx][sb])+,[olx]s',
        's': r'\g<1>,xs'
    },
    {  # 如果自己是女性,兄弟姐妹的兄弟就是自己的兄弟
        'exp': r'(,[mw0])(,[olx][sb])+,[olx]b',
        's': r'\g<1>,xb'
    },
    {  # 不知道性别，兄弟姐妹的兄弟是自己或兄弟
        'exp': r'^,[olx][sb],[olx]b(.+)?$',
        's': r'\g<1>#,xb\g<1>'
    },
    {  # 不知道性别，兄弟姐妹的姐妹是自己或姐妹
        'exp': r'^,[olx][sb],[olx]s(.+)?$',
        's': r'\g<1>#,xs\g<1>'
    },
    {  # 将复合称谓拆分
        'exp': r'^,x([sb])$',
        's': ',o\g<1>#,l\g<1>'
    },
    # 父母
    {  # 母亲的丈夫是自己的父亲
        'exp': r'm,h',
        's': 'f'
    },
    {  # 父亲的妻子是自己的母亲
        'exp': r'f,w',
        's': 'm'
    },
    {  # 兄弟的父母就是自己的父母
        'exp': r',[xol][sb](,[mf])',
        's': r'\g<1>'
    },
    # 父母的子女
    {  # 父母的女儿年龄判断是姐姐还是妹妹
        'exp': r',[mf],d&([ol])',
        's': ',\g<1>s'
    },
    {  # 父母的儿子年龄判断是哥哥还是弟弟
        'exp': r',[mf],s&([ol])',
        's': ',\g<1>b'
    },
    {  # 如果自己是男性,父母的儿子是自己或者兄弟
        'exp': r'^(.*)(,[fh1]|[xol]b),[mf],s(.*)$',
        's': r'\g<1>\g<2>,xb\g<3>#\g<1>\g<2>\g<3>'
    },
    {  # 如果自己是女性,父母的女儿是自己或者姐妹
        'exp': r'^(.*)(,[mw0]|[xol]s),[mf],d(.*)$',
        's': r'\g<1>\g<2>,xs\g<3>#\g<1>\g<2>\g<3>'
    },
    {  # 如果自己是女性,父母的儿子是自己兄弟
        'exp': r'(,[mw0]|[xol]s),[mf],s',
        's': r'\g<1>,xb'
    },
    {  # 如果自己是男性,父母的女儿是自己姐妹
        'exp': r'(,[fh1]|[xol]b),[mf],d',
        's': r'\g<1>,xs'
    },
    {  # 父母的儿子是自己或兄弟
        'exp': r'^,[mf],s(.+)?$',
        's': ',1\g<1>#,xb\g<1>'
    },
    {  # 父母的女儿是自己或者姐妹
        'exp': r'^,[mf],d(.+)?$',
        's': ',0\g<1>#,xs\g<1>'
    },
    # 孩子
    {  # 孩子的姐妹是自己的女儿(年龄判断)
        'exp': r',[ds]&o,ob',
        's': ',s&o'
    },
    {  # 孩子的姐妹是自己的女儿(年龄判断)
        'exp': r',[ds]&o,os',
        's': ',d&o'
    },
    {  # 孩子的兄弟是自己的儿子(年龄判断)
        'exp': r',[ds]&l,lb',
        's': ',s&l'
    },
    {  # 孩子的兄弟是自己的儿子(年龄判断)
        'exp': r',[ds]&l,ls',
        's': ',d&l'
    },
    {  # 孩子的姐妹是自己的女儿
        'exp': r',[ds](&[ol])?,[olx]s',
        's': ',d'
    },
    {  # 孩子的兄弟是自己的儿子
        'exp': r',[ds](&[ol])?,[olx]b',
        's': ',s'
    },
    # 夫妻
    {  # 自己是女性，女儿或儿子的妈妈是自己
        'exp': r'(,[mwd0](&[ol])?|[olx]s),[ds](&[ol])?,m',
        's': r'\g<1>'
    },
    {  # 自己是女性，女儿或儿子的爸爸是自己的丈夫
        'exp': r'(,[mwd0](&[ol])?|[olx]s),[ds](&[ol])?,f',
        's': r'\g<1>,h'
    },
    {  # 自己是男性，女儿或儿子的爸爸是自己
        'exp': r'(,[fhs1](&[ol])?|[olx]b),[ds](&[ol])?,f',
        's': r'\g<1>'
    },
    {  # 自己是男性，女儿或儿子的妈妈是自己的妻子
        'exp': r'(,[fhs1](&[ol])?|[olx]b),[ds](&[ol])?,m',
        's': r'\g<1>,w'
    },
    {  # 不知道性别，子女的妈妈是自己或妻子
        'exp': r'^,[ds],m(.+)?$',
        's': r'\g<1>#,w\g<1>'
    },
    {  # 不知道性别，子女的爸爸是自己或丈夫
        'exp': r'^,[ds],f(.+)?$',
        's': r'\g<1>#,h\g<1>'
    },
    {  # 夫妻的孩子就是自己的孩子
        'exp': r',[wh](,[ds])',
        's': r'\g<1>'
    },
    {  # 夫妻的对方是自己
        'exp': r',w,h|,h,w',
        's': ''
    },
    {  # 并列关系处理
        'exp': r'(.+)?\[(.+)\|(.+)\](.+)?',
        's': r'\g<1>\g<2>\g<4>#\g<1>\g<3>\g<4>'
    }
];

_data = {
    '': ['自己'],
    # 本家
    'f': ['爸爸'],
    'f,f': ['爷爷'],
    'f,f,f': ['曾祖父'],
    'f,f,xb': ['堂祖父'],
    'f,f,xb,w': ['堂祖母'],
    'f,f,xb,s&o': ['堂伯'],
    'f,f,xb,s&o,w': ['堂伯母'],
    'f,f,xb,s&l': ['堂叔'],
    'f,f,xb,s,w': ['堂婶'],
    'f,f,xb,d': ['堂姑'],
    'f,f,xb,d,h': ['堂姑父'],
    'f,f,xb,d,s&o': ['表兄'],
    'f,f,xb,d,s&l': ['表弟'],
    'f,f,xb,d,d&o': ['表姐'],
    'f,f,xb,d,d&l': ['表妹'],
    'f,f,xs,s&o': ['表伯父'],
    'f,f,xs,s&o,w': [ '表伯母'],
    'f,f,xs,s&l': [ '表叔父'],
    'f,f,xs,s&l,w': ['表叔母'],
    'f,f,xs,s,s': ['表兄弟'],
    'f,f,xs,s,d': ['表姐妹'],
    'f,f,xs,d': ['表姑妈'],
    'f,f,xs,d,h': ['表姑父'],
    'f,f,xs,d,s': ['表兄弟'],
    'f,f,xs,d,d': ['表姐妹'],
    'f,m': ['奶奶'],
    'f,m,xb': ['舅公'],
    'f,m,xb,w': ['舅婆'],
    'f,m,xb,s&o': ['表伯父'],
    'f,m,xb,s&o,w': ['表伯母'],
    'f,m,xb,s&l': ['表叔父'],
    'f,m,xb,s&l,w': ['表叔母'],
    'f,m,xb,s,s': ['从表兄弟'],
    'f,m,xb,s,d': ['从表姐妹'],
    'f,m,xb,d': ['舅表姑母'],
    'f,m,xb,d,h': ['舅表姑父'],
    'f,m,xb,d,s': ['表兄弟'],
    'f,m,xb,d,d': ['表姐妹'],
    'f,m,xs': ['姨奶奶'],
    'f,m,xs,h': ['姨公'],
    'f,m,xs,s&o': ['表伯'],
    'f,m,xs,s&o,w': ['表伯母'],
    'f,m,xs,s&l': ['表叔'],
    'f,m,xs,s&l,w': [ '表婶'],
    'f,m,xs,s,s': ['表兄弟'],
    'f,m,xs,s,d': ['表姐妹'],
    'f,m,xs,d,s': ['表兄弟'],
    'f,m,xs,d,d': ['表姐妹'],
    'f,xb,w,f': ['姻伯公'],
    'f,xb,w,m': ['姻伯婆'],
    'f,xb,w,xb': ['姻世伯'],
    'f,xb,w,xb,w': ['姻伯母'],
    'f,xb,w,xs': ['姻伯母'],
    'f,xb,w,xs,h': ['姻世伯'],
    'f,xb,s&o': ['堂哥'],
    'f,xb,s&o,w': ['堂嫂'],
    'f,xb,s&l': ['堂弟'],
    'f,xb,s&l,w': ['堂弟媳'],
    'f,xb,s,s': ['堂侄'],
    'f,xb,s,s,w': ['堂侄媳妇'],
    'f,xb,s,s,s': ['堂侄孙'],
    'f,xb,s,s,s,w': ['堂侄孙媳妇'],
    'f,xb,s,s,d': ['堂侄孙女'],
    'f,xb,s,s,d,h': ['堂侄孙女婿'],
    'f,xb,s,d': ['堂侄女'],
    'f,xb,s,d,h': ['堂侄女婿'],
    'f,xb,d&o': ['堂姐'],
    'f,xb,d&o,h': ['堂姐夫'],
    'f,xb,d&l': ['堂妹'],
    'f,xb,d&l,h': ['堂妹夫'],
    'f,xb,d,s': ['堂外甥'],
    'f,xb,d,d': ['堂外甥女'],
    'f,ob': ['伯父'],
    'f,ob,w': ['伯母'],
    'f,lb': ['叔叔'],
    'f,lb,w': ['婶婶'],
    # 姑家
    'f,xs': ['姑妈'],
    'f,xs,h': ['姑父'],
    'f,xs,s&o': [ '表哥'],
    'f,xs,s&o,w': ['表嫂'],
    'f,xs,s&l': [ '表弟'],
    'f,xs,s&l,w': ['表弟媳'],
    'f,xs,s,s': ['表侄'],
    'f,xs,s,s,s': ['表侄孙'],
    'f,xs,s,s,s,w': ['表侄孙媳妇'],
    'f,xs,s,s,d': ['表侄孙女'],
    'f,xs,s,s,d,h': ['表侄孙女婿'],
    'f,xs,s,d': ['表侄女'],
    'f,xs,d&o': [ '表姐'],
    'f,xs,d&o,h': ['表姐夫'],
    'f,xs,d&l': ['表妹'],
    'f,xs,d&l,h': ['表妹夫'],
    'f,xs,d,s': ['表外甥'],
    'f,xs,d,d': ['表外甥女'],
    'f,os': ['姑妈'],
    'f,ls': ['姑妈'],
    # 外家
    'm': ['妈妈'],
    'm,f': ['外公'],
    'm,f,xb,s': ['堂舅'],
    'm,f,xb,s,w': ['堂舅妈'],
    'm,f,xb,s,s&o': ['堂舅表兄'],
    'm,f,xb,s,s&l': ['堂舅表弟'],
    'm,f,xb,s,d&o': ['堂舅表姐'],
    'm,f,xb,s,d&l': ['堂舅表妹'],
    'm,f,xb,d': ['堂姨'],
    'm,f,xb,d,h': ['堂姨丈'],
    'm,f,xb,d,s&o': ['堂姨表兄'],
    'm,f,xb,d,s&l': ['堂姨表弟'],
    'm,f,xb,d,d&o': ['堂姨表姐'],
    'm,f,xb,d,d&l': ['堂姨表妹'],
    'm,f,xs': ['姑姥姥'],
    'm,f,xs,h': ['姑姥爷'],
    'm,f,xs,s': ['表舅'],
    'm,f,xs,s,w': ['表舅妈'],
    'm,f,xs,s,s': ['表兄弟'],
    'm,f,xs,s,d': ['表姐妹'],
    'm,f,xs,d': ['表姨妈'],
    'm,f,xs,d,h': ['表姨父'],
    'm,f,xs,d,s': ['表兄弟'],
    'm,f,xs,d,d': ['表姐妹'],
    'm,m': ['外婆'],
    'm,m,xb': ['舅公'],
    'm,m,xb,w': ['舅婆'],
    'm,m,xb,s': [ '表舅父'],
    'm,m,xb,s,w': ['表舅母'],
    'm,m,xb,s,s': ['表兄弟'],
    'm,m,xb,s,d': ['表姐妹'],
    'm,m,xb,d': ['表姨妈'],
    'm,m,xb,d,h': [ '表姨父'],
    'm,m,xb,d,s': ['表兄弟'],
    'm,m,xb,d,d': ['表姐妹'],
    'm,m,xs': ['姨姥'],
    'm,m,xs,h': ['姨公'],
    'm,m,xs,s': ['表舅'],
    'm,m,xs,s,w': [ '表舅妈'],
    'm,m,xs,s,s': ['表兄弟'],
    'm,m,xs,s,d': ['表姐妹'],
    'm,m,xs,d': ['姨表姨母'],
    'm,m,xs,d,h': ['姨表姨父'],
    'm,m,xs,d,s': ['表兄弟'],
    'm,m,xs,d,d': ['表姐妹'],
    # 舅家
    'm,xb': ['舅舅'],
    'm,xb,w': ['舅妈'],
    'm,xb,s&o': [ '表哥'],
    'm,xb,s&o,w': ['表嫂'],
    'm,xb,s&l': ['表弟'],
    'm,xb,s&l,w': ['表弟媳'],
    'm,xb,s,s': ['表侄'],
    'm,xb,s,s,s': ['表侄孙'],
    'm,xb,s,s,s,w': ['表侄孙媳妇'],
    'm,xb,s,s,d': ['表侄孙女'],
    'm,xb,s,s,d,h': ['表侄孙女婿'],
    'm,xb,s,d': ['表侄女'],
    'm,xb,d&o': ['表姐'],
    'm,xb,d&o,h': ['表姐夫'],
    'm,xb,d&l': [ '表妹'],
    'm,xb,d&l,h': ['表妹夫'],
    'm,xb,d,s': ['表外甥'],
    'm,xb,d,d': ['表外甥女'],
    'm,ob': ['大舅'],
    'm,ob,w': ['大舅妈'],
    'm,lb': ['小舅'],
    'm,lb,w': ['小舅妈'],
    # 姨家
    'm,xs': ['姨妈'],
    'm,xs,h': ['姨父'],
    'm,xs,s&o': [ '表哥'],
    'm,xs,s&o,w': ['表嫂'],
    'm,xs,s&l': [ '表弟'],
    'm,xs,s&l,w': ['表弟媳'],
    'm,xs,s,s': ['表侄'],
    'm,xs,s,s,s': ['表侄孙'],
    'm,xs,s,s,s,w': ['表侄孙媳妇'],
    'm,xs,s,s,d': ['表侄孙女'],
    'm,xs,s,s,d,h': ['表侄孙女婿'],
    'm,xs,s,d': ['表侄女'],
    'm,xs,s,d,s': ['外表侄孙'],
    'm,xs,s,d,s,w': ['外表侄孙媳妇'],
    'm,xs,s,d,d': ['外表侄孙女'],
    'm,xs,s,d,d,h': ['外表侄孙女婿'],
    'm,xs,d&o': ['表姐'],
    'm,xs,d&o,h': ['表姐夫'],
    'm,xs,d&l': ['表妹'],
    'm,xs,d&l,h': ['表妹夫'],
    'm,xs,d,s': ['表外甥'],
    'm,xs,d,d': ['表外甥女'],
    'm,os': ['大姨'],
    'm,os,h': ['大姨父'],
    'm,ls': ['小姨'],
    'm,ls,h': ['小姨父'],
    # 婆家
    'h': ['老公'],
    'h,f': ['公公'],
    'h,f,lb': ['叔公'],
    'h,f,lb,w': ['叔婆'],
    'h,f,xb,s&o': ['堂兄'],
    'h,f,xb,s&o,w': ['堂嫂'],
    'h,f,xb,s&l': ['堂弟'],
    'h,f,xb,s&l,w': ['堂弟媳妇'],
    'h,f,xb,d&o': ['堂大姑姐'],
    'h,f,xb,d&o,h': ['堂大姑姐夫'],
    'h,f,xb,d&l': ['堂小姑妹'],
    'h,f,xb,d&l,h': ['堂小姑妹夫'],
    'h,f,xb,d,s': ['堂夫甥男'],
    'h,f,xb,d,d': ['堂夫甥女'],
    'h,f,xs': ['姑婆'],
    'h,f,xs,h': ['姑公'],
    'h,m': ['婆婆'],
    'h,m,xb': ['舅公'],
    'h,m,xb,w': ['舅婆'],
    'h,m,xs': ['姨婆'],
    'h,m,xs,h': ['姨公'],
    'h,ob': ['大伯子'],
    'h,ob,w': ['大婶'],
    'h,lb': ['小叔'],
    'h,lb,w': ['小婶'],
    'h,xb,s': ['叔侄'],
    'h,os': ['大姑子'],
    'h,os,h': ['大姑夫'],
    'h,ls': ['小姑子'],
    'h,ls,h': ['小姑夫'],
    # 岳家
    'w': ['妻子'],
    'w,f': ['岳父'],
    'w,f,xb,s&o': ['堂大舅'],
    'w,f,xb,d&o': ['堂大姨'],
    'w,m': ['岳母'],
    'w,m,xb,s&o': ['表大舅'],
    'w,m,xb,d&o': ['表大姨'],
    'w,m,xs,s&o': ['表大舅'],
    'w,m,xs,d&o': ['表大姨'],
    'w,ob': ['大舅子'],
    'w,ob,w': ['舅嫂'],
    'w,lb': ['小舅子'],
    'w,lb,w': ['舅弟媳'],
    'w,os': ['大姨子'],
    'w,os,h': ['大姨夫'],
    'w,ls': ['小姨子'],
    'w,ls,h': ['小姨夫'],
    # 旁支
    'xb': ['兄弟'],
    'xb,s': ['侄子'],
    'xb,s,w': ['侄媳', '侄媳妇'],
    'xb,s,s': ['侄孙', '侄孙子'],
    'xb,s,s,w': ['侄孙媳'],
    'xb,s,s,s': ['侄曾孙'],
    'xb,s,s,s,w': ['侄曾孙媳'],
    'xb,s,s,d': ['侄曾孙女'],
    'xb,s,s,d,h': ['侄曾孙女婿'],
    'xb,s,d': ['侄孙女'],
    'xb,s,d,h': ['侄孙女婿'],
    'xb,d': ['侄女'],
    'xb,d,h': ['侄女婿'],
    'xb,d,s': ['外侄孙'],
    'xb,d,s,w': ['外侄孙媳妇'],
    'xb,d,d': ['外侄孙女'],
    'xb,d,d,h': ['外侄孙女婿'],
    'ob': ['哥哥'],
    'ob,w': ['嫂子'],
    'ob,w,f': ['姻伯父'],
    'ob,w,m': ['姻伯母'],
    'lb': ['弟弟'],
    'lb,w': ['弟妹'],
    'lb,w,f': ['姻叔父'],
    'lb,w,m': ['姻叔母'],
    'xs': ['姐妹'],
    'xs,h,f': ['姻世伯'],
    'xs,h,f,f': ['姻伯祖'],
    'xs,h,m': [ '亲家娘'],
    'xs,h,xb': ['姻兄/姻弟'],
    'xs,h,xs': ['姻姐/姻妹'],
    'xs,s': ['外甥'],
    'xs,s,w': ['外甥媳妇'],
    'xs,s,s': ['外甥孙'],
    'xs,s,s,w': ['外甥孙媳妇'],
    'xs,s,s,s': ['外曾甥孙'],
    'xs,s,s,d': ['外曾甥孙女'],
    'xs,s,d': ['外甥孙女'],
    'xs,s,d,h': ['外甥孙女婿'],
    'xs,s,d,s': ['外曾甥孙'],
    'xs,s,d,d': ['外曾甥孙女'],
    'xs,d': ['外甥女'],
    'xs,d,h': ['外甥女婿'],
    'xs,d,s': ['外甥孙'],
    'xs,d,s,w': ['外甥孙媳妇'],
    'xs,d,s,s': ['外曾甥孙'],
    'xs,d,s,d': ['外曾甥孙女'],
    'xs,d,d': ['外甥孙女'],
    'xs,d,d,h': ['外甥孙女婿'],
    'xs,d,d,s': ['外曾甥孙'],
    'xs,d,d,d': ['外曾甥孙女'],
    'os': ['姐姐'],
    'os,h': ['姐夫'],
    'ls': ['妹妹'],
    'ls,h': ['妹夫'],
    # 自家
    's': ['儿子'],
    's,w': ['儿媳妇'],
    's,w,xb': ['姻侄'],
    's,w,xb,s': ['姻侄孙'],
    's,w,xb,d': ['姻侄孙女'],
    's,w,xs': ['姻侄女'],
    's,w,xs,s': ['姻侄孙'],
    's,w,xs,d': ['姻侄孙女'],
    's,s': ['孙子'],
    's,s,w': ['孙媳妇'],
    's,s,s': ['曾孙'],
    's,s,s,w': ['曾孙媳妇'],
    's,s,d': ['曾孙女'],
    's,s,d,h': ['曾孙女婿'],
    's,d': ['孙女'],
    's,d,h': ['孙女婿'],
    's,d,s': ['曾外孙'],
    's,d,d': ['曾外孙女'],
    'd': ['女儿'],
    'd,h': ['女婿'],
    'd,s': ['外孙'],
    'd,s,w': ['外孙媳'],
    'd,s,s': ['外曾孙'],
    'd,s,d': ['外曾孙女'],
    'd,d': ['外孙女'],
    'd,d,h': ['外孙女婿'],
    'd,d,s': ['外曾外孙'],
    'd,d,d': ['外曾外孙女'],
    # 亲家
    's,w,m': ['亲家母'],
    's,w,f': ['亲家公'],
    's,w,f,ob': ['姻兄'],
    's,w,f,lb': ['姻弟'],
    's,w,f,os': ['姻姐'],
    's,w,f,ls': ['姻妹'],
    'd,h,m': ['亲家母'],
    'd,h,f': ['亲家公'],
    'd,h,f,ob': ['姻兄'],
    'd,h,f,lb': ['姻弟'],
}


def getSelectors(s):
    s = re.sub('/[二|三|四|五|六|七|八|九|十]{1,2}', 'x', s)
    lists = s.replace('我', '').replace('家的', '的').replace('家', '的').split('的')
    result = []  # 所有可能性
    match = True
    while lists:
        name = lists.pop(0)  # 当前匹配词
        arr = []  # 当前匹配词可能性
        has = False
        for i in _data:
            value = _data[i]
            if name in value:  # 是否存在该关系
                if i or not lists:  # 对‘我’的优化
                    arr.append(i)
                has = True
        if not has:
            match = False
        if result:  # 当前匹配词与之前可能性组合
            res = []
            for i in result:
                for j in arr:
                    res.append(i + ',' + j)
            result = res
        else:
            for i in arr:
                result.append(',' + i)

    return result if match else []


# 简化选择器
def selector2id(selector, sex):
    result = []
    rhash = {}
    if sex < 0:  # 如果自己的性别不确定
        if ',w' in selector == 0:
            sex = 1
        elif ',h' in selector == 0:
            sex = 0
    if sex > -1:
        selector = ',' + str(sex) + selector

    if re.search(r',[w0],w|,[h1],h', selector):
        return []
    def getId(selector):
        s = ''
        if selector not in rhash:
            rhash[selector] = True
            status = True
            while s != selector:
                s = selector
                for item in _filter:
                    selector = re.sub(item['exp'], item['s'], selector)
                    if '#' in selector:
                        arr = selector.split('#')
                        for j in arr:
                            getId(j)
                        status = False
                        break
            if status:
                if re.search(r',[w0],w|,[h1],h', selector):
                    return []
                selector = re.sub(r',[01]', '', selector)[1:]  # 去前面逗号和性别信息
                result.append(selector)

    getId(selector)
    return list(set(result))

# 获取数据
def getDataById(did):
    items = []
    flt = r'&[olx]'  # 忽略属性

    def getData(d):
        res = []
        for i in _data:
            if re.sub(flt, '', i) == d:
                res.append(_data[i][0])
        return res
    if did in _data:  # 直接匹配称呼
        items.append(_data[did][0])
    else:
        items = getData(did)
        if not items:  # 忽略年龄条件查找
            did = re.sub(r'&[ol]', '', did)
            items = getData(did)
        if not items:  # 忽略年龄条件查找
            did = re.sub(r'[ol]', 'x', did)
            items = getData(did)
        if not items:  # 缩小访问查找
            l = re.sub(r'x', 'l', did)
            items = getData(l)
            o = re.sub(r'x', 'o', did)
            items.extend(getData(o))
    return items


# 逆转ID
def reverseId(did, sex):
    rhash = {
        'f': ['d', 's'],
        'm': ['d', 's'],
        'h': ['w', ''],
        'w': ['', 'h'],
        's': ['m', 'f'],
        'd': ['m', 'f'],
        'lb': ['os', 'ob'],
        'ob': ['ls', 'lb'],
        'xb': ['xs', 'xb'],
        'ls': ['os', 'ob'],
        'os': ['ls', 'lb'],
        'xs': ['xs', 'xb']
    }
    age = ''
    if '&o' in did > -1:
        age = '&l'
    elif '&l' in did > -1:
        age = '&o'
    if did:
        did = re.sub(r'&[ol]', '', did)
        sex = 1 if sex else 0  # 逆转运算自身性别必须确定
        sid = re.sub(r',[fhs]|,[olx]b', ',1', (',' + str(sex) + ',' + did))
        sid = re.sub(r',[mwd]|,[olx]s', ',0', sid)
        sid = sid[1:sid.rindex(',')]
        id_arr = did.split(',')[::-1]
        sid_arr = sid.split(',')[::-1]
        arr = []
        for i, ia in enumerate(id_arr):
            arr.append(rhash[ia][int(sid_arr[i])])
        return ','.join(arr) + age
    return ''


# 获取关系链条
def getChainById(did):
    arr = did.split(',')
    items = []
    for i in arr:
        key = re.sub(r'&[ol]', '', i)
        items.append(_data[key][0])
    return '的'.join(items)


def get_relation(parameter):
    options = {
        'text': '',
        'sex': -1,
        'reverse': False
    }
    for p in parameter:
        options[p] = parameter[p]
    selectors = getSelectors(options['text'])
    result = []  # 匹配结果
    for s in selectors:  # 遍历所有可能性
        ids = selector2id(s, options['sex'])
        for i in ids:
                if options['reverse']:
                    i = reverseId(i, options['sex'])
                items = getDataById(i)
                if items:
                    result.extend(items)
                elif i[0] == 'w' or i[0] == 'h':
                    items = getDataById(i[2:])
                    if items:
                        result.extend(items)
    return list(set(result))
r = 0
s = 1
text = '我'
g = get_relation({'text':text, 'sex':s, 'reverse':r})