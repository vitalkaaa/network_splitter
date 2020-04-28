import netaddr


def main():
    with open('input.txt') as fi:
        includes, excludes = fi.read().split('\n\n')
        includes = [i for i in includes.split('\n')]
        excludes = [e for e in excludes.split('\n')]

        iset = netaddr.IPSet(includes)
        for e in excludes:
            if not e:
                continue

            enet = netaddr.IPNetwork(e)
            if '/32' in e:
                iset.remove(netaddr.IPRange(enet.ip, enet.ip))
            else:
                iset.remove(netaddr.IPRange(enet.ip, enet.broadcast))

    with open('output.txt', 'w') as fo:
        print('Results:')
        for i in iset.iter_ipranges():
            print(i)
            print(i, file=fo)


if __name__ == '__main__':
    main()