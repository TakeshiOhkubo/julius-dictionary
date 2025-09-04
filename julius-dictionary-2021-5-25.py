# for julius-dictation kit 4.5
# copyrighted by 大久保猛司 (Takeshi Ohkubo)
# Windows IME辞書(tsv)を変換.
# 「サイトメガロウイルス」「ガス壊疽うま毒素」等は1-column目の読みの平仮名発音区切にunderbar_挿入が必要 (ex. さいとめがろ_ういるす).
# 「21 trisomy」のようなspace挿入はjulius実行時にError.　「21_trisomy」に変換.
# 最後の行(line)に改行だけでの何も無い行が追加される問題。手動で削除が必要。


trichr  =['きゅう',    'きょう',    'ぎゅう',      'ぎょう',      'しゅう',    'しょう',      'じゅう',     'じょう',      'ぢゅう',     'ぢょう',     'ちゅう',     'ちょう',     'にゅう',     'にょう',     'ひゅう',     'ひょう',      'びゅう',     'びょう',      'ぴゅう',     'ぴょう',     'みゅう',      'みょう',     'りゅう',     'りょう']
c3_A    =['ky u:',     'ky o:',     'gy u',        'gy o',        'sh u:',     'sh o:',       'j u:',       'j o:',        'j u:',       'j o:',       'ch u:',      'ch o:',      'ny u:',      'ny o:',      'hy u:',      'hy o:',       'by u:',      'by o:',       'py u:',      'py o:',      'my u:',       'my o:',      'ry u:',      'ry o:' ]
c3_B    =['ky_B u:_I', 'ky_B o:_I', 'gy_B u:_I',   'gy_B o:_I',   'sh_B u:_I', 'sh_B o:_I',   'j_B u:_I',   'j_B o:_I',    'j_B u:_I',   'j_B o:_I',   'ch_B u:_I',  'ch_B o:_I',  'ny_B u:_I',  'ny_B o:_I',  'hy_B u:_I',  'hy_B o:_I',   'by_B u:_I',  'by_B o:_I',   'py_B u:_I',  'py_B o:_I',  'my_B u:_I',   'my_B o:_I',  'ry_B u:_I',  'ry_B o:_I']
c3_I    =['ky_I u:_I', 'ky_I o:_I', 'gy_I u:_I',   'gy_I o:_I',   'sh_I u:_I', 'sh_I o:_I',   'j_I u:_I',   'j_I o:_I',    'j_I u:_I',   'j_I o:_I',   'ch_I u:_I',  'ch_I o:_I',  'ny_I u:_I',  'ny_I o:_I',  'hy_I u:_I',  'hy_I o:_I',   'by_I u:_I',  'by_I o:_I',   'py_I u:_I',  'py_I o:_I',  'my_I u:_I',   'my_I o:_I',  'ry_I u:_I',  'ry_I o:_I']

bichr   =['えい',  'おう',  'きゃ',     'きゅ',     'きょ',     'ぎゃ',     'ぎゅ',     'ぎょ',     'くぃ',        'くぇ',        'くぉ',        'けい',     'こう',      'げい',     'ごう',     'しゃ',     'しぃ',     'しゅ',     'しぇ',     'しょ',     'じぁ',     'じゃ',     'じゅ',     'じぇ',    'じょ',     'すぃ',        'ずぃ',     'せい',     'そう',      'ぜい',     'ぞう',     'ちゃ',     'ちゅ',     'ちぇ',     'ちょ',     'つぁ',     'つぃ',     'つぇ',     'てぃ',     'でぃ',     'でゅ',     'とぅ',     'どぅ',      'てい',     'とう',      'でい',     'どう',     'にゃ',     'にゅ',     'にょ',     'ねい',     'のう',      'ヴぁ',     'ヴぃ',     'ヴぇ',     'ヴぉ',     'ひゃ',     'ひゅ',     'ひょ',     'へい',      'ほう',     'びゃ',     'びゅ',     'びょ',     'ぴゃ',     'ぴゅ',     'ぴょ',     'ふぁ',     'ふぃ',     'ふぇ',     'ふぉ',     'ふゅ',     'ふょ',     'へい',     'ほう',      'べい',     'ぼう',      'ぺい',     'ぽう',     'ほぃ',        'みゃ',     'みゅ',     'みょ',     'めい',     'もう',      'ゆう',     'よう',      'りゃ',     'りゅ',     'りょ',     'れい',     'ろう',      'うぃ',     'うぇ',     'うぉ',    'ヴぁ',     'ヴぃ',    'ヴぇ',    'ヴぉ',    'ヴゃ',     'ヴゅ',     'ヴょ']
c2_A    =['e:',    'o:',    'ky a',     'ky u',     'ky o',     'gy a',     'gy u',     'gy o',     'k u i',       'k u e',       'k u o',       'k e:',     'k o:',      'g e:',     'g o:',     'sh a',     'sh i',     'sh u',     'sh e',     'sh o',     'j a',      'j a',      'j u',      'j e',     'j o',      's u i',       'j i',      's e:',     's o:',      'z e:',     'z o:',     'ch a',     'ch u',     'ch e',     'ch o',     'ts a',     'ts i',     'ts e',     't i',      'd i',      'dy u',     't u',      'd u',       't e:',     't o:',      'd e:',     'd o:',     'ny a',     'ny u',     'ny o',     'n e:',     'n o:',      'b a',      'b i',      'b e',      'b o',      'hy a',     'hy u',     'hy o',     'h e:',      'h o:',     'by a',     'by u',     'by o',     'py a',     'py u',     'py o',     'f a',      'f i',      'f e',      'f o',      'hy u',     'hy o',     'h e:',     'h o:',      'b e:',     'b o:',      'p e:',     'p o:',     'h o i',       'my a',     'my u',     'my o',     'm e:',     'm o:',      'y u:',     'y o:',      'ry a',     'ry u',     'ry o',     'r e:',     'r o:',      'w i',      'w e',      'w o',     'b a',      'b i',     'b e',     'b o',     'by a',     'by u',     'by o' ]
c2_B    =['e:_B',  'o:_B',  'ky_B a_I', 'ky_B u_I', 'ky_B o_I', 'gy_B a_I', 'gy_B u_I', 'gy_B o_I', 'k_B u_I i_I', 'k_B u_I e_I', 'k_B u_I o_I', 'k_B e:_I', 'k_B o:_I',  'g_B e:_I', 'g_B o:_I', 'sh_B a_I', 'sh_B i_I', 'sh_B u_I', 'sh_B e_I', 'sh_B o_I', 'j_B a_I',  'j_B a_I',  'j_B u_I',  'j_B e_I', 'j_B o_I',  's_B u_I i_I', 'j_B i_I',  's_B e:_I', 's_B o:_I',  'z_B e:_I', 'z_B o:_I', 'ch_B a_I', 'ch_B u_I', 'ch_B e_I', 'ch_B o_I', 'ts_B a_I', 'ts_B i_I', 'ts_B e_I', 't_B i_I',  'd_B i_I',  'dy_B u_I', 't_B u_I',  'd_B u_I',   't_B e:_I', 't_B o:_I',  'd_B e:_I', 'd_B o:_I', 'ny_B a_I', 'ny_B u_I', 'ny_B o_I', 'n_B e:_I', 'n_B o:_I',  'b_B a_I',  'b_B i_I',  'b_B e_I',  'b_B o_I',  'hy_B a_I', 'hy_B u_I', 'hy_B o_I', 'h_B e:_I',  'h_B o:_I', 'by_B a_I', 'by_B u_I', 'by_B o_I', 'py_B a_I', 'py_B u_I', 'py_B o_I', 'f_B a_I',  'f_B i_I',  'f_B e_I',  'f_B o_I',  'hy_B u_I', 'hy_B o_I', 'h_B e:_I', 'h_B o:_I',  'b_B e:_I', 'b_B o:_I',  'p_B e:_I', 'p_B o:_I', 'h_B o_I i_I', 'my_B a_I', 'my_B u_I', 'my_B o_I', 'm_B e:_I', 'm_B o:_I',  'y_B u:_I', 'y_B o:_I',  'ry_B a_I', 'ry_B u_I', 'ry_B o_I', 'r_B e:_I', 'r_B o:_I',  'w_B i_I',  'w_B e_I',  'w_B o_I', 'b_B a_I',  'b_B i_I', 'b_B e_I', 'b_B o_I', 'by_B a_I', 'by_B u_I', 'by_B o_I']
c2_I    =['e:_I',  'o:_I',  'ky_I a_I', 'ky_I u_I', 'ky_I o_I', 'gy_I a_I', 'gy_I u_I', 'gy_I o_I', 'k_U u_I i_I', 'k_I u_I e_I', 'k_I u_I o_I', 'k_I e:_I', 'k_I o:_I',  'g_I e:_I', 'g_I o:_I', 'sh_I a_I', 'sh_I i_I', 'sh_I u_I', 'sh_I e_I', 'sh_I o_I', 'j_I a_I',  'j_I a_I',  'j_I u_I',  'j_I e_I', 'j_I o_I',  's_I u_I i_I', 'j_I i_I',  's_I e:_I', 's_I o:_I',  'z_I e:_I', 'z_I o:_I', 'ch_I a_I', 'ch_I u_I', 'ch_I e_I', 'ch_I o_I', 'ts_I a_I', 'ts_I i_I', 'ts_I e_I', 't_I i_I',  'd_I i_I',  'dy_I u_I', 't_I u_I',  'd_I u_I',   't_I e:_I', 't_I o:_I',  'd_I e:_I', 'd_I o:_I', 'ny_I a_I', 'ny_I u_I', 'ny_I o_I', 'n_I e:_I', 'n_I o:_I',  'b_I a_I',  'b_I i_I',  'b_I e_I',  'b_I o_I',  'hy_I a_I', 'hy_I u_I', 'hy_I o_I', 'h_I e:_I',  'h_I o:_I', 'by_I a_I', 'by_I u_I', 'by_I o_I', 'py_I a_I', 'py_I u_I', 'py_I o_I', 'f_I a_I',  'f_I i_I',  'f_I e_I',  'f_I o_I',  'hy_I u_I', 'hy_I o_I', 'h_I e:_I', 'h_I o:_I',  'b_I e:_I', 'b_I o:_I',  'p_I e:_I', 'p_I o:_I', 'h_I o_I i_I', 'my_I a_I', 'my_I u_I', 'my_I o_I', 'm_I e:_I', 'm_I o:_I',  'y_I u:_I', 'y_I o:_I',  'ry_I a_I', 'ry_I u_I', 'ry_I o_I', 'r_I e:_I', 'r_I o:_I',  'w_I i_I',  'w_I e_I',  'w_I o_I', 'b_I a_I',  'b_I i_I', 'b_I e_I', 'b_I o_I', 'by_I a_I', 'by_I u_I', 'by_I o_I']

monochr =['あ',   'い',   'う',   'え',  'お',  'ぁ',  'ぃ',  'ぅ',  'ぇ',   'ぉ',  'か',      'き',      'く',      'け',      'こ',      'が',      'ぎ',      'ぐ',      'げ',      'ご',      'さ',      'し',       'す',      'せ',      'そ',      'ざ',      'じ',      'ず',      'ぜ',      'ぞ',      'た',      'ち',       'つ',       'て',      'と',      'だ',      'ぢ',      'づ',      'で',      'ど',      'な',      'に',      'ぬ',      'ね',      'の',      'は',      'ひ',      'ふ',      'へ',      'ほ',      'ば',      'び',      'ぶ',      'べ',      'ぼ',      'ぱ',      'ぴ',      'ぷ',      'ぺ',      'ぽ',      'ま',      'み',      'む',      'め',      'も',      'や',      'ゆ',      'よ',      'ら',      'り',      'る',      'れ',      'ろ',      'わ',      'を',   'っ',   'ー', 'ん',  'ヴ',      'ゐ',   'ゑ']
c1_A    =['a',    'i',    'u',    'e',   'o',   'a',   'i',   'u',   'e',    'o',   'k a',     'k i',     'k u',     'k e',     'k o',     'g a',     'g i',     'g u',     'g e',     'g o',     's a',     'sh i',     's u',     's e',     's o',     'z a',     'j i',     'z u',     'z e',     'z o',     't a',     'ch i',     'ts u',     't e',     't o',     'd a',     'j i',     'z u',     'd e',     'd o',     'n a',     'n i',     'n u',     'n e',     'n o',     'h a',     'h i',     'f u',     'h e',     'h o',     'b a',     'b i',     'b u',     'b e',     'b o',     'p a',     'p i',     'p u',     'p e',     'p o',     'm a',     'm i',     'm u',     'm e',     'm o',     'y a',     'y u',     'y o',     'r a',     'r i',     'r u',     'r e',     'r o',     'w a',     'o',    'q',    ':',  'N',   'b u',     'i',    'e' ]
c1_B    =['a_B',  'i_B',  'u_B',  'e_B', 'o_B', 'a_B', 'i_B', 'u_B', 'e_B',  'o_B', 'k_B a_I', 'k_B i_I', 'k_B u_I', 'k_B e_I', 'k_B o_I', 'g_B a_I', 'g_B i_I', 'g_B u_I', 'g_B e_I', 'g_B o_I', 's_B a_I', 'sh_B i_I', 's_B u_I', 's_B e_I', 's_B o_I', 'z_B a_I', 'j_B i_I', 'z_B u_I', 'z_B e_I', 'z_B o_I', 't_B a_I', 'ch_B i_I', 'ts_B u_I', 't_B e_I', 't_B o_I', 'd_B a_I', 'j_B i_I', 'z_B u_I', 'd_B e_I', 'd_B o_I', 'n_B a_I', 'n_B i_I', 'n_B u_I', 'n_B e_I', 'n_B o_I', 'h_B a_I', 'h_B i_I', 'f_B u_I', 'h_B e_I', 'h_B o_I', 'b_B a_I', 'b_B i_I', 'b_B u_I', 'b_B e_I', 'b_B o_I', 'p_B a_I', 'p_B i_I', 'p_B u_I', 'p_B e_I', 'p_B o_I', 'm_B a_I', 'm_B i_I', 'm_B u_I', 'm_B e_I', 'm_B o_I', 'y_B a_I', 'y_B u_I', 'y_B o_I', 'r_B a_I', 'r_B i_I', 'r_B u_I', 'r_B e_I', 'r_B o_I', 'w_B a_I', 'o_B',  'q_B',  ':',  'N_B', 'b_B u_I', 'i_B',  'e_B']
c1_I    =['a_I',  'i_I',  'u_I',  'e_I', 'o_I', 'a_I', 'i_I', 'u_I', 'e_I',  'o_I', 'k_I a_I', 'k_I i_I', 'k_I u_I', 'k_I e_I', 'k_I o_I', 'g_I a_I', 'g_I i_I', 'g_I u_I', 'g_I e_I', 'g_I o_I', 's_I a_I', 'sh_I i_I', 's_I u_I', 's_I e_I', 's_I o_I', 'z_I a_I', 'j_I i_I', 'z_I u_I', 'z_I e_I', 'z_I o_I', 't_I a_I', 'ch_I i_I', 'ts_I u_I', 't_I e_I', 't_I o_I', 'd_I a_I', 'j_I i_I', 'z_I u_I', 'd_I e_I', 'd_I o_I', 'n_I a_I', 'n_I i_I', 'n_I u_I', 'n_I e_I', 'n_I o_I', 'h_I a_I', 'h_I i_I', 'f_I u_I', 'h_I e_I', 'h_I o_I', 'b_I a_I', 'b_I i_I', 'b_I u_I', 'b_I e_I', 'b_I o_I', 'p_I a_I', 'p_I i_I', 'p_I u_I', 'p_I e_I', 'p_I o_I', 'm_I a_I', 'm_I i_I', 'm_I u_I', 'm_I e_I', 'm_I o_I', 'y_I a_I', 'y_I u_I', 'y_I o_I', 'r_I a_I', 'r_I i_I', 'r_I u_I', 'r_I e_I', 'r_I o_I', 'w_I a_I', 'o_I',  'q_I',  ':',  'N_I', 'b_I u_I', 'i_I',  'e_I']

vwl1    =['a_E', 'a:_E', 'i_E', 'i:_E', 'u_E', 'u:_E', 'e_E', 'e:_E', 'o_E', 'o:_E']


def kana2IPA(c0, i):
    h1='';  h2=''
    # 3文字置換
    if i <= len(c0)-2 and len(c0) >= 3:
        if c0[i-1:i+2] in trichr:
            print(c0[i-1:i+2], '\t', end='')
            h1=c3_A[trichr.index(c0[i-1:i+2])]
            if i==1:
                h2=c3_B[trichr.index(c0[i-1:i+2])]
            else:
                h2=c3_I[trichr.index(c0[i-1:i+2])]
            return  h1, h2,  3
    # 2文字置換
    if i <= len(c0)-1 and len(c0) >= 2:
        if c0[i-1:i+1] in bichr:
            print(c0[i-1:i+1], '\t', end='')
            h1=c2_A[bichr.index(c0[i-1:i+1])]
            if i==1:
                h2=c2_B[bichr.index(c0[i-1:i+1])]
            else:
                h2=c2_I[bichr.index(c0[i-1:i+1])]
            return  h1, h2,  2
    # 1文字置換
    if c0[i-1] in monochr:
        print(c0[i-1], '\t', end='')
        h1=c1_A[monochr.index(c0[i-1])]
        if i==1:
            h2=c1_B[monochr.index(c0[i-1])]
        else:
            h2=c1_I[monochr.index(c0[i-1])]
        return  h1, h2,  1
    # どの文字にもmatchせず
    print('do not match any characters')
    h1='';  h2=''
    return  h1, h2,  1


iline1=1

#f1=open('./folder/test1-julius.txt', mode='rt', encoding='utf-8')
#f1=open('./folder/output-2021-3-22-improved.txt', mode='rt', encoding='utf-8')
f1=open('./folder/byoshokanri.txt', mode='rt', encoding='utf-8')
#f1=open('./folder/output1.txt', mode='rt', encoding='utf-8')
#f1=open('./folder/DMiME-1.1.txt', mode='rt', encoding='utf-8')

line=f1.readline()

while line:
    rec1=line.strip()
    rec1=rec1.split('\t');  c0=rec1[0]; c1=rec1[1]; c2=rec1[2]
    print(c1, '\t', iline1); iline1 += 1
    c1=c1.replace(' ', '_')    #  convert space to underscore.
    line=f1.readline()
    
    i=1  # 先頭～i文字目
    h1t=''; h2t=''
    
    while True:
        h1, h2,  sc1 = kana2IPA(c0,i)
        print(h1, '\t', h2)
        
        if i==1:
            h1t=h1;  h2t=h2
        else:
            if h1==':':
                h1t += ': '
                h2t = h2t[:-2] + ':_I'
            else:
                h1t += ' ' + h1;  h2t += ' ' + h2
        if i+sc1-1==len(c0):
            h2t=h2t[:-1] + 'E'
            break
        else:
            i += sc1

    if h2t in vwl1:
        h2t=h2t[:-1] + 'S'
        

    with open('./folder/bccwj.60k.htkdic',     mode='a', encoding='UTF8') as file1:
        file1.write(c1 + '+名詞' + '\t' + '[' + c1 + ']' + '\t' + h1t + '\n')

    with open('./folder/bccwj.60k.pdp.htkdic', mode='a', encoding='UTF8') as file2:
        file2.write(c1 + '+名詞' + '\t' + '[' + c1 + ']' + '\t' + h2t + '\n')

f1.close()
