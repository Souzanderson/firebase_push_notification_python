'''
####################################################################################
############# INSTRUÇÕES PARA UTILIZAÇÃO DO SENDER PUSHNOTIFICATION ################
####################################################################################
#                                                                                  #
#   - Coloque o arquivo ./beans/firebasemessage.py em um diretorio em seu projeto; #
#   - Adicione o arquivo de firebase_key.json apropriado na raiz do projeto;       #
#   - Siga o exemplo de utilização abaixo;                                         #
#                                                                                  #
####################################################################################
####################################################################################
'''


from beans.firebasemessage import PushNotification, MessagePushNotification

# @param topic => tópico para envio e recepção de mensagens, existem 3 tópicos configurados: lines, system, user_<idUser>
# @param title => título da notificação no mobile
# @param body => corpo da mensagem da notificação recebida no mobile
agent = MessagePushNotification(topic="bundy_cwb_lines", title= "Mensagem direcionada a todos", body= "Mensagem direcionada a todos!")

# @param message_agent => objeto contendo a mensagem para envio
# @param credentials_location => arquivo de autenticação com o servidor de push notification (padrão firebase_key.json)
# @def send => envia a mensagem usando oa rquivo de configuração 
PushNotification(message_agent = agent).send()