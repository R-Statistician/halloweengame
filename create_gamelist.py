import pandas as pd
import numpy as np

p = pd.read_csv('player_countries.csv')

p.head(1)

s = pd.read_csv('country_passphrase_hiddenpairs_static.csv')

def subset_pairs(p,s):
  return s[s['Country'].isin(p['Country'])]

info = subset_pairs(p,s)

players = [f'Player {str(i)}' for i in range(1,len(info)]

agent_names = ["Agent " + i for i in [
    'Skeleton','Monster','Zombie','Vampyr','Werewolf', 
    'Gargoyle','Djinni','Daemon','Golem','Phantom',
    'Specter','Mummy','Warlock','Scarecrow','Banshee',
    'Gravestone','Cryptic','Broomstick','Cauldron','Cobweb',''
    'Nevermore','Nightmare','Spellbound','Broomstick','Gorecrow',
    
    'Horror','Casket','Occult','Medusa','Marionette',
    'Corsair','Hobgoblin','Jackolantern','Reaper','Talisman',
    'Hellhound','Omen','Bewitched','Ritual','Harvestmoon',
    'Pentagram','Gallows','Raven','Vigil','Candlejack',
    'Haunting','Shapeshift','Voudou','Batwing','Macabre'
]
              ]

info['AgentName'] = agent_names[0:len(info)]

def generate_target_list(agent_list):
    # assert agent_list = agent_names, 'input list of agents'

    agent_pool = list(agent_list)

    target_list = []
    
    for agent in agent_list:
        while True and len(agent_pool) > 1:
            target = np.random.choice(agent_pool)
            if target != agent:
                target_list.append(target)
                agent_pool.remove(target)
                break
            
    return target_list + agent_pool

def generate_contact_list(agent_list):
    # assert agent_list = agent_names, 'input list of agents'
    assert 'Target' in info.columns, 'First create a target list'

    contact_pool = list(agent_list)
    contact_pool2 = list(agent_list)

    targets = info.Target

    first_contact = []
    second_contact = []
    
    for agent in agent_list:
        while True and len(contact_pool) > 1:
            contact1 = np.random.choice(contact_pool)

            if contact1 != agent and contact1 != str(info[info.AgentName == agent]['Target'].values[0]):
                first_contact.append(
                    f'The delegate from {info[info.AgentName == contact1]['Country'].values[0]} is {info[info.AgentName == contact1]['AgentName'].values[0]}')
                contact_pool.remove(contact1)
                break
     
    for agent in range(len(agent_list)):
        while True and len(contact_pool2) > 1:       
            contact2 = np.random.choice(contact_pool2)

            print(str(" ".join(first_contact[agent].split(' ')[-2:])))
            if contact2 != agent_list[agent] and contact2 != str(info[info.AgentName == agent_list[agent]]['Target'].values[0]) and contact2 != str(" ".join(first_contact[agent].split(' ')[-2:])):
                second_contact.append(
                    f'The delegate from {info[info.AgentName == contact2]['Country'].values[0]} is {info[info.AgentName == contact2]['AgentName'].values[0]}')
                contact_pool2.remove(contact2)
                break

    firstcontact = first_contact + contact_pool
    secondcontact = second_contact + contact_pool2

    boo = 0
    
    for c in range(len(firstcontact)):
        if firstcontact[c] == secondcontact[c]:
            boo += 1
    
    if boo > 0:
        generate_contact_list(agent_list)
    else:
        return firstcontact, secondcontact



info['Target'] = ["Your target is " + item for item in generate_target_list(agent_list=info.AgentName)]
firstcontact, secondcontact = generate_contact_list(info.AgentName)


info['FirstContact'] = firstcontact
info['SecondContact'] = secondcontact

# checks for collisions
for line in range(len(info)): 
    if info.at[line,'FirstContact'] == info.at[line,'SecondContact']:
        print("Boo!", line)

# corrects last line to match syntax
info.at[len(info)-1,'FirstContact'] = f'The delegate from {info.at[len(info)-1,'Country']} is {info.at[len(info)-1,'FirstContact']}'
info.at[len(info)-1,'SecondContact'] = f'The delegate from {info.at[len(info)-1,'Country']} is {info.at[len(info)-1,'SecondContact']}'

info.to_csv('Dynamic_gamelist.csv')
