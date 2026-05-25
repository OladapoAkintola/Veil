# cython: boundscheck=False, wraparound==false, initializedcheck=false
from libc.string cimport memcpy

cdef padlock(str src_path, str dst_path, const unsigned char[:] key):
    cdef int key_len = len(key)
    cdef int i= 0
    cdef unsigned char byte

    with open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
        chunk = src.read(65536)
        while chunk:
            cdef unsigned char[:] buf = bytearray(chunk)
            cdef int chunk_len = len(buf)
            cdef bytearray out = bytearray(chunk_len)
            cdef unsigned char[:] out_view = out

            for j in range(chunk_len):
                out_view[j] = buf[j] ^ key[i % key_len]
                i += 1

            dst.write(bytes(out))
            chunk = src.read(65536)