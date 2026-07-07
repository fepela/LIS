# -*- coding: utf-8 -*-
import base64, os
BASE="/tmp/claude-0/-home-user-LIS/f1c60334-9bd0-598b-8a65-bbc0dd016f5c/scratchpad"
def b64(p):
    with open(p,"rb") as f: return base64.b64encode(f.read()).decode()
fonts={400:"fonts/Poppins-Regular.ttf",500:"fonts/Poppins-Medium.ttf",600:"fonts/Poppins-SemiBold.ttf",700:"fonts/Poppins-Bold.ttf",800:"fonts/Poppins-ExtraBold.ttf"}
faces="\n".join(f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(data:font/ttf;base64,{b64(os.path.join(BASE,p))}) format('truetype');}}" for w,p in fonts.items())
logo_color="data:image/png;base64,"+b64(os.path.join(BASE,"logo_color.png"))
PET="#1A334A";PAR="#18A3B7";CIA="#27E6EC";SLATE="#51637A"

def photo_cover(chip,h1,sub,fotodesc):
    return f'''<section class="wcard">
 <div class="photo"><div class="ph-ic">📷</div><div class="ph-t">ÁREA DE FOTO</div><div class="ph-d">{fotodesc}</div></div>
 <div class="body">
   <div class="chip">{chip}</div>
   <h1>{h1}</h1>
   <p class="lead">{sub}</p>
 </div>
 <div class="wfoot"><img class="fl" src="{logo_color}"><div class="handle">@chapteria</div><div class="save">arraste →</div></div>
</section>'''

cards=[
 photo_cover("IA NO TRABALHO",
   'O Claude está virando <span class="mark">colega de trabalho</span>?',
   "A nova geração de IA não quer só responder. Quer executar.",
   "Ambiente de trabalho moderno; laptop com uma interface de IA/agente em execução na tela. Luz natural, clima executivo e limpo."),
 photo_cover("IA NA VIDA REAL",
   'Ele usou o ChatGPT para tentar <span class="mark">salvar a cachorra</span>.',
   "O que esse caso ensina sobre usar IA de verdade.",
   "Pessoa em casa, ao lado de um cachorro, mexendo no notebook/celular. Tom emocional, acolhedor, luz quente."),
 photo_cover("O PRÓXIMO CAPÍTULO DA IA",
   'Pare de perguntar.<br>Comece a <span class="mark">delegar</span>.',
   "A IA parou de só responder. Começou a executar tarefas inteiras.",
   "Mesa de trabalho vista de cima; mãos digitando, telas com um fluxo/agente trabalhando sozinho. Minimalista, tons neutros."),
]

CSS=f'''
{faces}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}}
.wcard{{position:relative;width:1080px;height:1350px;padding:0;overflow:hidden;display:flex;flex-direction:column;background:#fff;color:{PET}}}
.photo{{height:660px;margin:56px 56px 0;border-radius:34px;background:#e9eef2;border:2px dashed #c4d0d8;
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#8aa0ad}}
.ph-ic{{font-size:80px;filter:grayscale(.2);opacity:.8}}
.ph-t{{font-weight:800;font-size:30px;letter-spacing:.14em;margin-top:14px;color:#7f96a4}}
.ph-d{{font-weight:500;font-size:26px;line-height:1.4;max-width:640px;margin-top:16px;color:#93a6b2}}
.body{{padding:44px 90px 0}}
.chip{{display:inline-block;font-weight:700;font-size:23px;letter-spacing:.14em;color:#fff;background:{PAR};padding:13px 26px;border-radius:100px}}
h1{{font-weight:800;font-size:74px;line-height:1.06;letter-spacing:-.02em;margin-top:26px}}
.mark{{background:linear-gradient(transparent 58%, rgba(39,230,236,.45) 58%);padding:0 4px}}
.lead{{font-weight:500;font-size:38px;line-height:1.36;margin-top:26px;color:{SLATE};max-width:900px}}
.wfoot{{margin-top:auto;display:flex;align-items:center;gap:22px;border-top:2px solid #e8edf1;margin:0 90px;padding:34px 0 54px}}
.wfoot .fl{{height:42px}}
.handle{{font-weight:700;font-size:30px;color:{PET}}}
.save{{margin-left:auto;font-weight:600;font-size:28px;color:{PAR}}}
'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(cards)}</body></html>'
open(os.path.join(BASE,"wf2.html"),"w").write(html)
print("ok")
