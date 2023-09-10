class MirrorMacroAut():
    def __init__(self, nome):
        self.nome = nome

    def generateImport(self):
        import_str = f"from macros.Automacao.{self.nome}.home import start as start"
        return import_str.strip()

    def generateRoute(self):
        mirror = f"""
    @group_automacao.route("/{self.nome}/<req_id>/<req_name>/<user>")
    def macro_{self.nome}_index(req_id, req_name, user):
        try:
            retorno = start(req_id, req_name, user)
            return retorno
        except Exception as err:
            return str(err), 500
    """
        return mirror