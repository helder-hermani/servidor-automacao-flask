class MirrorMacroApi():
    def __init__(self, nome):
        self.nome = nome

    def generateImport(self):
        import_str = f"import macros.Api.{self.nome}.index as {self.nome}"
        return import_str.strip()

    def generateRoute(self, metodo):
        mirror = f"""
    @group_macro_api.{metodo}(\"/{self.nome}\")
    def macro_api_{self.nome}():
        try:
            resultado = {self.nome}.index(request)
            return jsonify(resultado), 200
        except Exception as err:
            resultado = {{
                \"status\": \"error\",
                \"message\": f'Erro ao processar a requisição: {{str(err)}}'
            }}
            return json.dumps(resultado, ensure_ascii=False).encode('utf-8'), 500
    """
        return mirror