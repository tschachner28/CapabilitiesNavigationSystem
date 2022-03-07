import networkx as nx

# key: node ID (int), value: node description (string)
def getNodeMappings():
        node_mappings = {
            # top level nodes (broadest categories)
            0: 'root', 1: 'Networking Operations', 2: 'Processes and Logging', 3: 'Files', 4: 'Memory Operations',
            5: 'Resource Limits', 6: 'I/O Port Operations', 7: 'System Startup Controls', 8: 'Kernel Modules',
            9: 'Virtual Terminal Operations', 10: 'Clock', 11: 'Performance', 12: 'Socket operations (only)',
            13: 'Firewall, socket, and other network operations', 14: 'BPF operations',
            15: 'Use RAW and PACKET sockets, or bind to any address for transparent proxying',
            16: 'Bind a socket to ports or listen to ports', 17: 'CAP_NET_ADMIN',
            18: 'BPF operations with performance implications', 19: 'Other BPF operations', 20: 'CAP_BPF', 21: 'CAP_NET_RAW',
            22: 'CAP_NET_BIND_SERVICE', 23: 'Performance monitoring of processes and CPUs',
            24: 'BPF operations that have performance implications', 25: 'CAP_PERFMON',
            26: 'Processes and Process Accounting', 27: 'Read contents of symbolic links to mapped files for processes',
            28: 'IDs', 29: 'PIDs', 30: 'GIDs', 31: 'Determine the PID allocated to the next process created in a namespace',
            32: 'CAP_CHECKPOINT_RESTORE', 33: 'Manipulate process GIDs and supplementary GID list',
            34: 'Forge GID when passing socket credentials via UNIX domain sockets',
            35: 'Write group ID mapping in a user namespace', 36: 'CAP_SETGID', 37: 'UIDs',
            38: 'Manipulate process GIDs and supplementary GID list', 39: 'CAP_SETUID',
            40: 'Enable or disable process accounting', 41: 'CAP_SYS_PACCT',
            42: 'Forge GID when passing socket credentials via UNIX domain sockets',
            43: 'Bypass permission checks for sending signals to processes', 44: 'CAP_KILL',
            45: 'Write group ID mapping in a user namespace', 46: 'Process/Thread Capabilities',
            47: 'Add any capability from the calling thread\'s bounding set to its inheritable set',
            48: 'Drop capabilities from bounding set', 49: 'Change securebits flags', 50: 'CAP_SETPCAP',
            51: 'Trace/inspect processes or transfer data between process address spaces ', 52: 'CAP_SYS_PTRACE',
            53: 'Set process nice value, scheduling policies and priorities, CPU affinity, or I/O scheduling class and priority',
            54: 'Move pages in a process to another set of nodes', 55: 'CAP_SYS_NICE', 56: 'Kernel logs',
            57: 'Open, close, read, or clear logs', 58: 'Enable,  disable, or limit console log messages',
            59: 'View kernel addresses exposed via /proc and other interfaces', 60: 'CAP_SYSLOG', 61: 'Kernel Auditing and Logs',
            62: 'Kernel auditing', 63: 'Read audit log via multicast netlink socket', 64: 'Write records to kernel auditing log',
            65: 'CAP_AUDIT_READ', 66: 'CAP_AUDIT_WRITE', 67: 'Other kernel auditing operations', 68: 'CAP_AUDIT_CONTROL',
            69: 'Bypass file read, write, and execute permission checks',
            70: 'Bypass file read, write, and execute permission checks',
            71: 'Bypass file read permission checks and directory read and execute permission checks',
            72: 'Bypass permission checks on operations that normally require the process\'s filesystem UID to match the filesystem\'s UID',
            73: 'CAP_DAC_OVERRIDE', 74: 'CAP_DAC_READ_SEARCH', 75: 'Open file handles or create file links',
            76: 'Open a file corresponding to a handle and return an open file descriptor',
            77: 'Create a link to a file referred to by a file descriptor',
            78: 'File flags and operations requiring or involving sticky bit', 79: 'Set inode flags on arbitrary files',
            80: 'Ignore directory sticky bit on file deletion',
            81: 'Modify user extended attributes on sticky directory owned by any user',
            82: 'Specify O_NOATIME to prevent updating the file last access time when the file is read',
            83: 'Set FS_APPEND_FL and FS_IMMUTABLE_FL flags', 84: 'Set other inode flags', 85: 'CAP_FOWNER',
            86: 'CAP_LINUX_IMMUTABLE', 87: 'Access control', 88: 'Set Access Control Lists on arbitrary files',
            89: 'Set-user-id and set-group-id mode bits', 90: 'MAC', 91: 'CAP_FSETID',
            92: 'Allow MAC configuration or state changes', 93: 'Override MAC', 94: 'CAP_MAC_ADMIN', 95: 'CAP_MAC_OVERRIDE',
            96: 'Other file operations', 97: 'Set arbitrary file capabilities',
            98: 'Change root directory or mount namespace', 99: ' Establish leases on arbitrary files',
            100: 'ext2 or ext3 operations', 101: 'CAP_SETFCAP', 102: 'CAP_SYS_CHROOT', 103: 'CAP_LEASE',
            104: 'Create special files', 105: 'CAP_MKNOD', 106: 'Processes', 107: 'Lock memory',
            108: 'Allocate memory using huge pages', 109: 'Bypass permission checks for operations on System V IPC objects',
            110: 'Modify certain kernel memory map descriptor fields of the calling process', 111: 'Other memory operations',
            112: 'CAP_IPC_LOCK', 113: 'CAP_IPC_OWNER', 114: 'CAP_SYS_RESOURCE', 115: 'CAP_SYS_RAWIO', 116: 'Block system suspend',
            117: 'Reboot', 118: 'Enable/disable Cntrl+Alt+Del', 119: 'Load a new kernel for later execution',
            120: 'Trigger something that will wake up the system', 121: 'CAP_BLOCK_SUSPEND', 122: 'CAP_SYS_BOOT',
            123: 'CAP_WAKE_ALARM', 124: 'Load/unload kernel modules', 125: 'CAP_SYS_MODULE', 126: 'CAP_SYS_TTY_CONFIG',
            127: 'Set system clock or real-time hardware clock', 128: 'CAP_SYS_TIME',
            129: 'Allow more than 64hz interrupts from the real-time clock'
        }
        return node_mappings

# Returns digraph object with edges
def getDigraph():
    DG = nx.DiGraph()
    DG.add_edges_from(
        [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9), (0,10), (0,11),
         (1,12), (1,13), (12,14), (12,15), (12,16), (12,34), (12,42), (12,63), (14,18), (14,19), (15,21), (16,22),
         (19,20), (18,25), (11,23), (11,24), (23,25), (24,25), (13,17), (2,26), (2,61), (26,27), (26,28), (26,40),
         (26,43), (26,46), (26,51), (26,53), (26,54), (27,32), (28,29), (28,30), (28,37), (29,31), (31,32), (30,33),
         (30,34), (30,35), (33,36), (34,36), (35,36), (37,38), (37,42), (37,45), (38,39), (42,39), (45,39), (40,41),
         (43,44), (46,47), (46,48), (46,49), (47,50), (48,50), (49,50), (61,56), (61,62), (56,57), (56,58), (56,59),
         (57,60), (58,60), (59,60), (51,52), (53,55), (54,55), (62,63), (62,64), (62,67), (63,65), (64,66), (67,68),
         (3,69), (3,75), (3,78), (3,87), (3,96), (69,70), (69,71), (69,72), (70,73), (71,74), (76,74), (77,74), (72,85),
         (75,76), (75,77), (78,79), (78,80), (78,81), (78,82), (79,83), (80,85), (81,85), (82,85), (88,85), (83,86),
         (84,85), (87,88), (87,89), (87,90), (89,91), (90,92), (90,93), (92,94), (93,95), (96,97), (96,98), (96,99),
         (96,100), (96,104), (97,101), (98,102), (99,103), (104,105), (4,106), (4,107), (4,108), (4,109), (4,110),
         (4,111), (106,51), (106,54), (106,53), (107,112), (108,112), (109,113), (100,114), (110,114), (5,114), (111,115),
         (6,115), (7,116), (7,117), (7,118), (7,119), (7,120), (116,121), (117,122), (118,122), (119,122), (120,123),
         (129,114), (8,124), (124,125), (9,126), (10,127), (10,129), (127,128)])
    return DG