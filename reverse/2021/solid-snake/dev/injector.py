# IDEA:
# 1. make jump from end of PyOS_Readline to our small checker code
# 2. Checker check sequence such as "unlock('<flag>')"
# 3. If correct this code runs shellcode with argument wich containts user input

shellcode = b"\xF3\x0F\x1E\xFA\x55\x48\x89\xE5\x89\x7D\xFC\x48\x89\x75\xF0\x89\x55\xF8\x48\x31\xC0\x48\xFF\xC0\x0F\x05\x90\x5D\xC3\xF3\x0F\x1E\xFA\x55\x48\x89\xE5\x89\x7D\xDC\x89\x75\xD8\x48\x89\x55\xD0\xC7\x45\xF4\x04\x00\x00\x00\x48\xC7\x45\xF8\x00\x00\x00\x00\xEB\x56\x8B\x45\xD8\x89\x45\xE4\x8B\x45\xD8\xC1\xE0\x06\x89\xC2\x8B\x45\xD8\xC1\xE8\x08\x31\xC2\x8B\x45\xDC\x8D\x34\x02\x8B\x4D\xF4\x48\x8B\x45\xF8\xBA\x00\x00\x00\x00\x48\xF7\xF1\x48\x89\xD0\x48\x8D\x14\x85\x00\x00\x00\x00\x48\x8B\x45\xD0\x48\x01\xD0\x8B\x00\x8D\x14\x06\x48\x8B\x45\xF8\x01\xD0\x01\x45\xD8\x8B\x45\xE4\x89\x45\xDC\x48\x83\x45\xF8\x01\x8B\x45\xF4\x83\xC0\x08\xC1\xE0\x02\x89\xC0\x48\x39\x45\xF8\x72\x99\x48\xC7\x45\xE8\x00\x00\x00\x00\x8B\x45\xDC\x48\xC1\xE0\x20\x48\x01\x45\xE8\x8B\x45\xD8\x48\x01\x45\xE8\x48\x8B\x45\xE8\x5D\xC3\xF3\x0F\x1E\xFA\x55\x48\x89\xE5\x48\x83\xEC\x60\x48\x89\x7D\xA8\x89\x75\xA4\x48\x8B\x04\x25\x00\x00\x40\x00\x48\x8B\x14\x25\x08\x00\x40\x00\x48\x89\x45\xE0\x48\x89\x55\xE8\x48\xB8\xE3\xD2\x01\x81\x69\x62\xB8\x8E\x48\x89\x45\xC0\x48\xB8\x92\xE3\xA8\xD8\x75\x2D\x4D\xB9\x48\x89\x45\xC8\x48\xB8\x5C\x62\x2F\xE1\x55\x9A\x3A\xAE\x48\x89\x45\xD0\x48\xB8\x47\x54\xA4\xFA\x63\xD5\x8E\x59\x48\x89\x45\xD8\xC7\x45\xFC\x00\x00\x00\x00\xC7\x45\xF8\x04\x00\x00\x00\xEB\x5F\x8B\x45\xF8\x48\x63\xD0\x48\x8B\x45\xA8\x48\x01\xD0\x8B\x00\x89\x45\xB8\x8B\x45\xF8\x48\x98\x48\x8D\x50\x04\x48\x8B\x45\xA8\x48\x01\xD0\x8B\x00\x89\x45\xBC\x8B\x4D\xBC\x8B\x45\xB8\x48\x8D\x55\xE0\x89\xCE\x89\xC7\xE8\xA9\xFE\xFF\xFF\x48\x89\x45\xF0\x8B\x45\xFC\x8D\x50\x01\x89\x55\xFC\x48\x98\x48\x8B\x44\xC5\xC0\x48\x39\x45\xF0\x74\x07\xB8\x00\x00\x00\x00\xEB\x14\x83\x45\xF8\x08\x8B\x45\xA4\x83\xE8\x01\x39\x45\xF8\x7C\x96\xB8\x01\x00\x00\x00\xC9\xC3\xF3\x0F\x1E\xFA\x55\x48\x89\xE5\x48\x89\x7D\xF8\x48\x31\xC0\x80\x3F\x00\x74\x08\x48\xFF\xC0\x48\xFF\xC7\xEB\xF3\x90\x90\x5D\xC3\xF3\x0F\x1E\xFA\x55\x48\x89\xE5\x48\x83\xEC\x20\x48\x89\x7D\xE8\x48\x8B\x45\xE8\x48\x89\xC7\xE8\xC4\xFF\xFF\xFF\x89\x45\xFC\x8B\x45\xFC\x48\x98\x48\x8D\x50\xFF\x48\x8B\x45\xE8\x48\x01\xD0\x0F\xB6\x00\x3C\x0A\x75\x50\x8B\x45\xFC\x48\x98\x48\x8D\x50\xFE\x48\x8B\x45\xE8\x48\x01\xD0\x0F\xB6\x00\x3C\x29\x75\x39\x8B\x45\xFC\x48\x98\x48\x8D\x50\xFD\x48\x8B\x45\xE8\x48\x01\xD0\x0F\xB6\x00\x3C\x22\x75\x22\x8B\x45\xFC\x48\x98\x48\x8D\x50\xFD\x48\x8B\x45\xE8\x48\x01\xD0\xC6\x00\x00\x48\x8B\x45\xE8\x48\x89\xC7\xE8\x5D\xFF\xFF\xFF\x89\x45\xFC\xC7\x45\xFC\x25\x00\x00\x00\x8B\x55\xFC\x48\x8B\x45\xE8\x89\xD6\x48\x89\xC7\xE8\x5E\xFE\xFF\xFF\x85\xC0\x74\x16\xBA\x07\x00\x00\x00\xBE\xFE\xBD\x76\x00\xBF\x01\x00\x00\x00\xE8\x7F\xFD\xFF\xFF\xEB\x14\xBA\x09\x00\x00\x00\xBE\xB1\x2C\x71\x00\xBF\x01\x00\x00\x00\xE8\x69\xFD\xFF\xFF\xB8\x00\x00\x00\x00\xC9\xC3"

# rax contains user input   
'''mov rbx, qword ptr [rax]
push 0x22286b636f6c6e75
pop rcx
cmp rbx, rcx
'''

shellcode_inejction_offset = 0x2A8C50
checker_injection_offset = 0x2467C

checker = b"\x4c\x8b\x7d\x00\x49\xbe\x75\x6e\x6c\x6f\x63\x6b\x28\x22\x4d\x39\xf7\x75\x16\x48\x89\xef\x48\x83\xc7\x08\x48\xc7\xc0\x50\x8c\x6a\x00\x48\x05\xcb\x01\x00\x00\xff\xd0\x5a\x48\x89\xe8\x5b\x5d\x41\x5c\x41\x5d\x41\x5e\x41\x5f\xc3"
target = "python3.9"

orig_data = open(target, 'rb').read()

fd = open(target + "_patch", "wb")
fd.write(orig_data[:checker_injection_offset])
fd.write(checker)
fd.write(orig_data[checker_injection_offset + len(checker):shellcode_inejction_offset])
fd.write(shellcode)
fd.write(orig_data[shellcode_inejction_offset + len(shellcode):])
fd.close()