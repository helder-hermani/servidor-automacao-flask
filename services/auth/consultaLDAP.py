from ldap3 import Server, Connection, ALL

# def pegaDadosLdap(user, password):
#     objLdap = Ldap(user,password)
#     try:
#         ldapUser = objLdap.consultaMatricula(user)
#         if (ldapUser != None):
#             return (f"{user} - {ldapUser['no-usuario']} \n" \
#             f"{ldapUser['no-funcao']} \n" \
#             f"{ldapUser['no-unidade']}")
#         else:
#             raise Exception
#     except Exception as err:
#         return('Não foi possível recuperar as informações do usuário na rede da Caixa. \n'
#                f'Continuando execução apenas com as credenciais CIWEB - Usuário {user}.')


class Ldap:
    def __init__(self, user, password):
        self.success = False
        try:
            ldap_server = 'ldap://ldapcluster.corecaixa:489'
            ldap_port = 489  # ou 636 se for SSL
            ldap_dn = 'ou=People,o=caixa'
            ldap_user = user
            ldap_password = password

            # Cria conexão com o servidor LDAP
            server = Server(ldap_server, port=ldap_port, get_info=ALL)
            user_dn = "uid="+ldap_user+","+ldap_dn
            self.conn = Connection(server, user=user_dn, password=ldap_password, auto_bind='NO_TLS')
            print('Usuário validado com sucesso!')
            self.success = True
        except Exception as err:
            print('Erro na conexão com o servidor LDAP. Não é possível validar usuário.')
            return None

    def consultaMatricula(self, matricula):
        filtro = f'(&(objectClass=person)(uid={matricula}))'
        base_dn = 'ou=People,o=caixa'
        attributes = ['dn','uid','nu-cpf','no-usuario','no-funcao','nu-funcao','co-unidade','no-unidade','nu-lotacaofisica','no-lotacaofisica','dt-nascimento','mail']  # lista de atributos retorno

        dadosLdap=self.conn.search(base_dn, filtro, attributes=attributes)

        if (dadosLdap):
            # return self.conn.entries
            return {
                'matricula':self.conn.entries[0]['uid'][0],
                'nu-cpf':self.conn.entries[0]['nu-cpf'][0],
                'no-usuario': self.conn.entries[0]['no-usuario'][0],
                'no-funcao': self.conn.entries[0]['no-funcao'][0],
                'nu-funcao': self.conn.entries[0]['nu-funcao'][0],
                'co-unidade': self.conn.entries[0]['co-unidade'][0],
                'no-unidade': self.conn.entries[0]['no-unidade'][0],
                'nu-lotacaofisica': self.conn.entries[0]['nu-lotacaofisica'][0],
                'no-lotacaofisica': self.conn.entries[0]['no-lotacaofisica'][0],
                'dt-nascimento': self.conn.entries[0]['dt-nascimento'][0],
                'mail': self.conn.entries[0]['mail'][0],
            }
        else:
            return None
        
    def consultaCpf(self, cpf):
        filtro = f'(&(objectClass=person)(nu-cpf={cpf}))'
        base_dn = 'ou=People,o=caixa'
        attributes = ['dn','uid','nu-cpf','no-usuario','no-funcao','nu-funcao','co-unidade','no-unidade','nu-lotacaofisica','no-lotacaofisica','dt-nascimento','mail']  # lista de atributos que você deseja retornar

        dadosLdap=self.conn.search(base_dn, filtro, attributes=attributes)

        if (dadosLdap):
            # return self.conn.entries
            return {
                'matricula':self.conn.entries[0]['uid'][0],
                'nu-cpf':self.conn.entries[0]['nu-cpf'][0],
                'no-usuario': self.conn.entries[0]['no-usuario'][0],
                'no-funcao': self.conn.entries[0]['no-funcao'][0],
                'nu-funcao': self.conn.entries[0]['nu-funcao'][0],
                'co-unidade': self.conn.entries[0]['co-unidade'][0],
                'no-unidade': self.conn.entries[0]['no-unidade'][0],
                'nu-lotacaofisica': self.conn.entries[0]['nu-lotacaofisica'][0],
                'no-lotacaofisica': self.conn.entries[0]['no-lotacaofisica'][0],
                'dt-nascimento': self.conn.entries[0]['dt-nascimento'][0],
                'mail': self.conn.entries[0]['mail'][0],
            }
        else:
            return None

    
    def fechaConexao(self):
        self.conn.unbind()
