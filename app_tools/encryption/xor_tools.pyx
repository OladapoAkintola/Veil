# cython: boundscheck=False, wraparound=False, initializedcheck=False
from libc.string cimport memcpy

cdef str _padlock(str src_path, str dst_path, const unsigned char[:] key):
    cdef int key_len = len(key)
    cdef int i = 0
    cdef int j
    cdef int chunk_len
    cdef unsigned char[:] buf
    cdef unsigned char[:] out_view
    cdef bytearray out

    with open(src_path, 'rb') as src, open(dst_path, 'wb') as dst:
        chunk = src.read(65536)
        while chunk:
            buf = bytearray(chunk)
            chunk_len = len(buf)
            out = bytearray(chunk_len)
            out_view = out

            for j in range(chunk_len):
                out_view[j] = buf[j] ^ key[i % key_len]
                i += 1

            dst.write(bytes(out))
            chunk = src.read(65536)

    return dst_path

cpdef str padlock(str src_path, str dst_path, const unsigned char[:] key):
    _padlock(src_path, dst_path, key)