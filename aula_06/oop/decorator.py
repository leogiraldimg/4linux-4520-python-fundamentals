def grito_de_torcida(fn):
  def funcao_decorada(*args, **kwargs):
    print("VAAAAAI ...", end = " ") # injetar funcionalidades padrão
    return fn()
  return funcao_decorada

@grito_de_torcida
def grito_do_guarani():
  print('BUGRE!')

@grito_de_torcida
def grito_sampaio_correia():
  print("BOLIVIA QUERIDA!!!")

# @grito_de_torcida
# .....
